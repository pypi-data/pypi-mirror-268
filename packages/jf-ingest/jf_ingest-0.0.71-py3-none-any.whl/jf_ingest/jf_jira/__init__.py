import logging
from enum import Enum
from typing import Generator
from jf_ingest import diagnostics, logging_helper
from jf_ingest.config import IngestionConfig, IngestionType, IssueMetadata, JiraAuthMethod, IssueListForDownload, \
    IssueDownloadingResult, JiraDownloadConfig
from jf_ingest.constants import Constants
from jf_ingest.file_operations import IngestIOHelper, SubDirectory
from jf_ingest.jf_jira.auth import get_jira_connection
from jf_ingest.jf_jira.downloaders import (
    download_all_issue_metadata,
    download_boards_and_sprints,
    download_fields,
    download_issuelinktypes,
    download_issues,
    download_issuetypes,
    download_priorities,
    download_projects_and_versions_and_components,
    download_resolutions,
    download_statuses,
    download_users,
    download_worklogs,
    get_ids_from_difference_of_issue_metadata,
    get_jira_search_batch_size, get_issue_list_to_download, get_out_of_date_issue_ids,
    detect_issues_needing_re_download, download_issues_from_new_sync,
)
from jf_ingest.utils import batch_iterable_by_bytes_size

from jira import JIRA


logger = logging.getLogger(__name__)


class JiraObject(Enum):
    JiraFields = "jira_fields"
    JiraProjectsAndVersions = "jira_projects_and_versions"
    JiraUsers = "jira_users"
    JiraResolutions = "jira_resolutions"
    JiraIssueTypes = "jira_issuetypes"
    JiraLinkTypes = "jira_linktypes"
    JiraPriorities = "jira_priorities"
    JiraBoards = "jira_boards"
    JiraSprints = "jira_sprints"
    JiraBoardSprintLinks = "jira_board_sprint_links"
    JiraIssues = "jira_issues"
    JiraIssuesIdsDownloaded = "jira_issue_ids_downloaded"
    JiraIssuesIdsDeleted = "jira_issue_ids_deleted"
    JiraWorklogs = "jira_worklogs"
    JiraStatuses = "jira_statuses"


def load_issues_in_batches(
        issues_to_download: Generator[dict, None, None],
        ingest_io_helper: IngestIOHelper,
        ingest_config: IngestionConfig
) -> IssueDownloadingResult:
    """ given a generator object for issues to download; save them to disk in batches according to maximum size

    Args:
        issues_to_download: Generator object for issues to download
        ingest_io_helper: IngestIOHelper object for doing file operations
        ingest_config (IngestionConfig): A dataclass that holds several different configuration args for this task

    Return:
        IssueDownloadingResult: A dataclass that holds the results of the download;
            - the ids for jira issues retrieved,
            - jira_ids for parents of those retrieved issues,
            - and the total number of batches it took
    """
    total_issue_batches = 0
    all_downloaded_issue_ids = set()
    collected_parent_ids = set()

    for batch_number, batch_issues in enumerate(
        batch_iterable_by_bytes_size(
            issues_to_download, batch_byte_size=Constants.JIRA_ISSUES_UNCOMPRESSED_FILE_SIZE
        )
    ):
        logging_helper.send_to_agent_log_file(
            f'Saving {len(batch_issues)} issues as batch number {batch_number}',
        )
        all_downloaded_issue_ids.update(set(issue['id'] for issue in batch_issues))
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraIssues.value,
            subdirectory=SubDirectory.JIRA,
            json_data=batch_issues,
            batch_number=batch_number,
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )
        total_issue_batches += 1

        # we need to download parents of issues we just fetched
        collected_parent_ids.update(
            set(issue['fields']['parent']['id'] for issue in batch_issues if 'parent' in issue['fields'].keys()))

    return IssueDownloadingResult(
        discovered_parents=collected_parent_ids,
        downloaded_ids=all_downloaded_issue_ids,
        total_batches=total_issue_batches
    )


def pull_issues_old_metadata_path(
    jira_connect_or_fallback_connection: JIRA,
    jira_basic_connection: JIRA,
    jira_issues_batch_size: int,
    jira_config: JiraDownloadConfig,
    projects_and_versions: list[dict],
    ingest_io_helper: IngestIOHelper,
    ingest_config: IngestionConfig,
):
    """ "Default" old path for pulling issues
        get all metadata from jira, compare with metadata from JF, decide what to pull based on that
    Args:
        jira_connect_or_fallback_connection: either the basic connection or the special atlassian connect keys
        jira_basic_connection: definitely the basic connection (user/pass)
        jira_issues_batch_size: batch size to use for actually downloading issues (much lower than the 10k for IDs)
        jira_config: jira config for jf_ingest from JF
        projects_and_versions: list of projects and versions to pull issues from
        ingest_io_helper: IngestIOHelper object for doing file operations
        ingest_config: full jf_ingest config
    """

    logging_helper.send_to_agent_log_file("Running 100 batched sync path")
    logging_helper.send_to_agent_log_file(
        f"All issue operations will use a batch_size of {jira_issues_batch_size}",
    )

    #######################################################################
    # Pull Issue Metadata
    #######################################################################
    issue_metadata_from_jira: list[IssueMetadata] = download_all_issue_metadata(
        # We need jira 3.1.x to use connect: https://github.com/pycontribs/jira/pull/1157
        # So for now force basic auth.
        jira_connection=jira_basic_connection,
        project_keys=[
            proj["key"]
            for proj in projects_and_versions
            if proj["key"] not in jira_config.exclude_projects
        ],
        earliest_issue_dt=jira_config.earliest_issue_dt,
        num_parallel_threads=jira_config.issue_download_concurrent_threads,
        batch_size=jira_issues_batch_size,
    )

    issues_generator = download_issues(
        jira_connection=jira_connect_or_fallback_connection,
        full_redownload=jira_config.full_redownload,
        issue_download_concurrent_threads=jira_config.issue_download_concurrent_threads,
        jira_issues_batch_size=jira_issues_batch_size,
        issue_metadata_from_jellyfish=jira_config.jellyfish_issue_metadata,
        issue_metadata_from_jira=issue_metadata_from_jira,
        include_fields=jira_config.include_fields,
        exclude_fields=jira_config.exclude_fields,
    )

    all_downloaded_issue_ids = []
    total_issue_batches = 0

    for batch_number, batch_issues in enumerate(
            batch_iterable_by_bytes_size(
                issues_generator, batch_byte_size=Constants.JIRA_ISSUES_UNCOMPRESSED_FILE_SIZE
            )
    ):
        logging_helper.send_to_agent_log_file(
            f'Saving {len(batch_issues)} issues as batch number {batch_number}',
        )
        all_downloaded_issue_ids.extend([issue['id'] for issue in batch_issues])
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraIssues.value,
            subdirectory=SubDirectory.JIRA,
            json_data=batch_issues,
            batch_number=batch_number,
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )
        total_issue_batches += 1

    logger.info(
        f"Successfully saved {len(all_downloaded_issue_ids)} Jira Issues in {total_issue_batches} separate batches, "
        f"with each batch limited to "
        f"{round(Constants.JIRA_ISSUES_UNCOMPRESSED_FILE_SIZE / Constants.MB_SIZE_IN_BYTES)}MB per batch"
    )

    # Write Issues
    ingest_io_helper.write_json_to_local_or_s3(
        object_name=JiraObject.JiraIssuesIdsDownloaded.value,
        json_data=[int(issue_id) for issue_id in all_downloaded_issue_ids],
        subdirectory=SubDirectory.JIRA,
        save_locally=ingest_config.save_locally,
        upload_to_s3=ingest_config.upload_to_s3,
    )

    deleted_issue_ids = get_ids_from_difference_of_issue_metadata(
        jira_config.jellyfish_issue_metadata, issue_metadata_from_jira
    )

    return all_downloaded_issue_ids, deleted_issue_ids


def pull_issues_new_sync_path(
    jira_connect_or_fallback_connection: JIRA,
    jira_basic_connection: JIRA,
    jira_config: JiraDownloadConfig,
    projects_and_versions: list[dict],
    jira_issues_batch_size: int,
    ingest_io_helper: IngestIOHelper,
    ingest_config: IngestionConfig,
):
    """ Pulls issues using the "new" sync path, based on our ability to pull 10,000 jira issue IDs at one time
        as long as you only ask for `id` and `key` in the returned fields. Because we get no more fields we detect
        deletes as the absence of an issue on remote which we have local, and key changes as id match key mismatch
    Args:
        jira_connect_or_fallback_connection: either the basic connection or the special atlassian connect keys
        jira_basic_connection: definitely the basic connection (user/pass)
        jira_config: jira config for jf_ingest from JF
        projects_and_versions: list of projects and versions to pull issues from
        jira_issues_batch_size: batch size to use for actually downloading issues (much lower than the 10k for IDs)
        ingest_io_helper: IngestIOHelper object for doing file operations
        ingest_config: full jf_ingest config

    """

    logging_helper.send_to_agent_log_file("Running 10k batched sync path")
    # get list of issues to download from remote
    issues_to_download: IssueListForDownload = get_issue_list_to_download(
        # We need jira 3.1.x to use connect: https://github.com/pycontribs/jira/pull/1157
        # So for now force basic auth
        jira_connection=jira_basic_connection,
        jellyfish_issue_metadata=jira_config.jellyfish_issue_metadata,
        project_key_to_id={
            proj["key"]: proj["id"]
            for proj in projects_and_versions
            if proj["key"] not in jira_config.exclude_projects
            },
        earliest_issue_dt=jira_config.earliest_issue_dt,
        full_redownload=jira_config.full_redownload,
        issue_ids_for_redownload=set(str(i) for i in jira_config.jellyfish_issue_ids_for_redownload),
    )

    issues_generator = download_issues_from_new_sync(
        jira_connection=jira_connect_or_fallback_connection,
        issue_download_concurrent_threads=jira_config.issue_download_concurrent_threads,
        jira_issues_batch_size=jira_issues_batch_size,
        issues_to_download=issues_to_download,
        include_fields=jira_config.include_fields,
        exclude_fields=jira_config.exclude_fields,
    )
    download_results: IssueDownloadingResult = load_issues_in_batches(issues_generator, ingest_io_helper, ingest_config)
    # don't need to download parents of issues that already were fetched
    to_be_downloaded_parents = download_results.discovered_parents - download_results.downloaded_ids
    logger.info(f'Found {len(to_be_downloaded_parents)} parent issues to download')
    logger.info(f"Some of them are: {sorted(list(to_be_downloaded_parents))[:30]}")
    logger.info(
        f"Successfully saved {len(download_results.downloaded_ids)} Jira Issues in "
        f"{download_results.total_batches} separate batches, with each batch limited to "
        f"{round(Constants.JIRA_ISSUES_UNCOMPRESSED_FILE_SIZE / Constants.MB_SIZE_IN_BYTES)}MB per batch"
    )

    all_downloaded_ids = download_results.downloaded_ids

    # fetch parents
    if to_be_downloaded_parents:
        issues_generator = download_issues_from_new_sync(
            jira_connection=jira_connect_or_fallback_connection,
            issue_download_concurrent_threads=jira_config.issue_download_concurrent_threads,
            jira_issues_batch_size=jira_issues_batch_size,
            issues_to_download=IssueListForDownload(to_be_downloaded_parents, [], []),
            include_fields=jira_config.include_fields,
            exclude_fields=jira_config.exclude_fields,
        )
        results_after_parents: IssueDownloadingResult = load_issues_in_batches(
            issues_generator,
            ingest_io_helper,
            ingest_config
        )

        all_downloaded_ids.update(results_after_parents.downloaded_ids)

        # we don't believe these are necessary, but maybe TODO: consider making this recursive?
        more_parents = (
                results_after_parents.discovered_parents
                - results_after_parents.downloaded_ids
                - download_results.downloaded_ids
        )
        if more_parents:
            logger.info(f"Found {len(more_parents)} MORE parent issues to download. Skipping these.")
            logger.info(f"Some of them are: {sorted(list(more_parents))[:30]}")

    # Write Issues
    ingest_io_helper.write_json_to_local_or_s3(
        object_name=JiraObject.JiraIssuesIdsDownloaded.value,
        json_data=[int(issue_id) for issue_id in all_downloaded_ids],
        subdirectory=SubDirectory.JIRA,
        save_locally=ingest_config.save_locally,
        upload_to_s3=ingest_config.upload_to_s3,
    )

    return all_downloaded_ids, issues_to_download.id_to_key_deleted


@diagnostics.capture_timing()
@logging_helper.log_entry_exit()
def load_and_push_jira_to_s3(ingest_config: IngestionConfig):
    """Loads data from JIRA, Dumps it to disk, and then uploads that data to S3

    All configuration for this object is done via the JIRAIngestionConfig object

    Args:
        config (IngestionConfig): A dataclass that holds several different configuration args for this task

    Returns:
        bool: Returns True on Success
    """

    # For Agent, we leverage the DEBUG log level for some things that are really INFO level. We do this
    # because we want to keep the output console in Agent as clean as possible, and we don't want to
    # interrupt the TQDM progress bar
    #
    # When we run this code in Prefect, however, we lose the DEBUG level logs because Prefect logging is
    # pretty rigid and hard to set with fine granularity. To get around this problem, use logger.log with
    # a variable log level
    logging_helper._set_ingestion_type(ingest_config.ingest_type)
    logger.info('Beginning load_and_push_jira_to_s3')
    if not ingest_config.save_locally and not ingest_config.upload_to_s3:
        logger.error(
            f'Configuration error! Ingestion configuration must have either save_locally or upload_to_s3 set to True!'
        )
        raise Exception(
            'Save Locally and Upload to S3 are both set to False! Set one to true or no data will be saved!'
        )

    jira_config = ingest_config.jira_config
    if jira_config.skip_issues and jira_config.only_issues:
        logger.warning(f"only_issues and skip_issues are both True, so all tasks will be skipped. ")
        return False

    logging_helper.send_to_agent_log_file(f"Feature flags: {jira_config.feature_flags}")

    #######################################################################
    # SET UP JIRA CONNECTIONS (Basic and Potentially Atlassian Connect)
    #######################################################################
    jira_basic_connection = get_jira_connection(
        config=jira_config, auth_method=JiraAuthMethod.BasicAuth
    )

    jira_atlas_connect_connection = (
        get_jira_connection(config=jira_config, auth_method=JiraAuthMethod.AtlassianConnect)
        if JiraAuthMethod.AtlassianConnect in jira_config.available_auth_methods
        else None
    )
    # There is an ongoing effort to cut all things over to Atlassian Connect only,
    # but it is a piecewise migration for now.
    # OJ-29745
    jira_connect_or_fallback_connection = jira_basic_connection

    if jira_config.feature_flags.get("lusca-auth-always-use-connect-for-atlassian-apis-Q423"):
        logging_helper.send_to_agent_log_file("Will use connect for most API calls")
        jira_connect_or_fallback_connection = jira_atlas_connect_connection
    else:
        logging_helper.send_to_agent_log_file("Will use basic auth for most API calls")

    #######################################################################
    # Init IO Helper
    #######################################################################
    ingest_io_helper = IngestIOHelper(ingest_config=ingest_config)

    S3_OR_JELLYFISH_LOG_STATEMENT = (
        's3' if ingest_config.ingest_type == IngestionType.DIRECT_CONNECT else 'jellyfish'
    )
    if ingest_config.save_locally:
        logger.info(f"Data will be saved locally to: {ingest_io_helper.local_file_path}")
    else:
        logger.info("Data will not be saved locally")
    if ingest_config.upload_to_s3:
        logger.info(f"Data will be submitted to {S3_OR_JELLYFISH_LOG_STATEMENT}")
    else:
        logger.info(f"Data will NOT be submitted to {S3_OR_JELLYFISH_LOG_STATEMENT}")

    #######################################################################
    # Jira Projects
    #######################################################################
    projects_and_versions = download_projects_and_versions_and_components(
        jira_connection=jira_connect_or_fallback_connection,
        is_agent_run=ingest_config.ingest_type == IngestionType.AGENT,
        jellyfish_project_ids_to_keys=jira_config.jellyfish_project_ids_to_keys,
        jellyfish_issue_metadata=jira_config.jellyfish_issue_metadata,
        include_projects=jira_config.include_projects,
        exclude_projects=jira_config.exclude_projects,
        include_categories=jira_config.include_project_categories,
        exclude_categories=jira_config.exclude_project_categories,
    )

    project_ids = {proj["id"] for proj in projects_and_versions}
    ingest_io_helper.write_json_to_local_or_s3(
        object_name=JiraObject.JiraProjectsAndVersions.value,
        json_data=projects_and_versions,
        subdirectory=SubDirectory.JIRA,
        save_locally=ingest_config.save_locally,
        upload_to_s3=ingest_config.upload_to_s3,
    )

    if not jira_config.only_issues:
        #######################################################################
        # Jira Fields
        #######################################################################
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraFields.value,
            subdirectory=SubDirectory.JIRA,
            json_data=download_fields(
                jira_connect_or_fallback_connection,
                jira_config.include_fields,
                jira_config.exclude_fields,
            ),
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        ######################################################################
        # Jira Users
        #######################################################################
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraUsers.value,
            subdirectory=SubDirectory.JIRA,
            json_data=download_users(
                jira_basic_connection=jira_basic_connection,  # Use BasicAuth because /users/search is not supported by Connect apps.
                jira_atlas_connect_connection=jira_atlas_connect_connection
                if jira_config.should_augment_emails
                else None,  # Use AtlasConnect for 'augment with email' subtask
                gdpr_active=jira_config.gdpr_active,
                search_users_by_letter_email_domain=jira_config.search_users_by_letter_email_domain,
                required_email_domains=jira_config.required_email_domains,
                is_email_required=jira_config.is_email_required,
            ),
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        #######################################################################
        # Jira Resolutions
        #######################################################################
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraResolutions.value,
            subdirectory=SubDirectory.JIRA,
            json_data=download_resolutions(jira_connect_or_fallback_connection),
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        #######################################################################
        # Jira Issue Types
        #######################################################################
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraIssueTypes.value,
            subdirectory=SubDirectory.JIRA,
            json_data=download_issuetypes(
                jira_connect_or_fallback_connection, project_ids=project_ids
            ),
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        #######################################################################
        # Jira Link Types
        #######################################################################
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraLinkTypes.value,
            subdirectory=SubDirectory.JIRA,
            json_data=download_issuelinktypes(jira_connect_or_fallback_connection),
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        #######################################################################
        # Jira Priorities
        #######################################################################
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraPriorities.value,
            subdirectory=SubDirectory.JIRA,
            json_data=download_priorities(jira_connect_or_fallback_connection),
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        #######################################################################
        # Jira Statuses
        #######################################################################
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraStatuses.value,
            subdirectory=SubDirectory.JIRA,
            json_data=download_statuses(jira_connect_or_fallback_connection),
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        #######################################################################
        # Jira Boards, Sprints, and Links
        #######################################################################
        boards, sprints, links = download_boards_and_sprints(
            jira_connect_or_fallback_connection,
            jira_config.download_sprints,
        )
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraBoards.value,
            subdirectory=SubDirectory.JIRA,
            json_data=boards,
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraSprints.value,
            subdirectory=SubDirectory.JIRA,
            json_data=sprints,
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraBoardSprintLinks.value,
            subdirectory=SubDirectory.JIRA,
            json_data=links,
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

    if not jira_config.skip_issues:

        # For Jira Issue operations we need to determine the batch size that
        # the JIRA provider will limit us to
        jira_issues_batch_size = get_jira_search_batch_size(
            jira_connection=jira_connect_or_fallback_connection,
            optimistic_batch_size=jira_config.issue_batch_size,
        )

        # check if this company is on new ingest path, default to False
        if jira_config.feature_flags.get(Constants.NEW_SYNC_FF_NAME, False):
            all_downloaded_issue_ids, all_deleted_issue_ids = pull_issues_new_sync_path(
                jira_connect_or_fallback_connection,
                jira_basic_connection,
                jira_config,
                projects_and_versions,
                jira_issues_batch_size,
                ingest_io_helper,
                ingest_config,
            )
        else:
            all_downloaded_issue_ids, all_deleted_issue_ids = pull_issues_old_metadata_path(
                jira_connect_or_fallback_connection,
                jira_basic_connection,
                jira_issues_batch_size,
                jira_config,
                projects_and_versions,
                ingest_io_helper,
                ingest_config,
            )

        logger.info(f'{len(all_deleted_issue_ids)} issues have been detected as being deleted')
        # Write issues that got deleted
        ingest_io_helper.write_json_to_local_or_s3(
            object_name=JiraObject.JiraIssuesIdsDeleted.value,
            subdirectory=SubDirectory.JIRA,
            json_data=list(all_deleted_issue_ids),
            save_locally=ingest_config.save_locally,
            upload_to_s3=ingest_config.upload_to_s3,
        )

        #######################################################################
        # Jira Work Logs
        #######################################################################
        if jira_config.download_worklogs:
            ingest_io_helper.write_json_to_local_or_s3(
                object_name=JiraObject.JiraWorklogs.value,
                subdirectory=SubDirectory.JIRA,
                json_data=download_worklogs(
                    jira_connect_or_fallback_connection,
                    all_downloaded_issue_ids,
                    jira_config.work_logs_pull_from,
                ),
                save_locally=ingest_config.save_locally,
                upload_to_s3=ingest_config.upload_to_s3,
            )
    else:
        logger.info(
            f"Skipping issues and worklogs bc config.skip_issues is {jira_config.skip_issues}"
        )

    if ingest_config.save_locally:
        logger.info(f"Data has been saved locally to: {ingest_io_helper.local_file_path}")
    else:
        logger.info(
            f"Data has not been saved locally, because save_locally was set to false in the ingest config!"
        )

    if ingest_config.upload_to_s3:
        logger.info(f"Data has been submitted to {S3_OR_JELLYFISH_LOG_STATEMENT}")
    else:
        logger.info(f"Data was not submitted to {S3_OR_JELLYFISH_LOG_STATEMENT}")

    return True
