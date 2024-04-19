import logging

import click
from gitlab_ps_utils.api import GitLabApi
from gitlab_evaluate.migration_readiness.gitlab.report_generator import ReportGenerator as GLReportGenerator
from gitlab_evaluate.migration_readiness.gitlab import evaluate as evaluate_api
from gitlab_evaluate.migration_readiness.jenkins.report_generator import ReportGenerator as JKReportGenerator

@click.command
@click.option("-s", "--source", help="Source URL: REQ'd")
@click.option("-t", "--token", help="Personal Access Token: REQ'd")
@click.option("-o", "--output", is_flag=True, help="Output Per Project Stats to screen")
@click.option("-i", "--insecure", is_flag=True, help="Set to ignore SSL warnings.")
@click.option("-g", "--group", help="Group ID. Evaluate all group projects (including sub-groups)")
@click.option("-f", "--filename", help="CSV Output File Name. If not set, will default to 'evaluate_output.xlsx'")
@click.option("-p", "--processes", help="Number of processes. Defaults to number of CPU cores")
def evaluate_gitlab(source, token, output, insecure, group, filename, processes):
    logging.basicConfig(filename='evaluate.log', level=logging.DEBUG)
    if None not in (token, source):

        if insecure:
            gitlabApi = GitLabApi(ssl_verify=False)
        else:
            gitlabApi = GitLabApi()

        evaluateApi = evaluate_api.EvaluateApi(gitlabApi)

        rg = GLReportGenerator(source, token, filename=filename,
                             output_to_screen=output, evaluate_api=evaluateApi, processes=processes)

        rg.get_app_stats(source, token, group)
        print("App stat retrieval complete. Moving on to Project metadata retrieval")
        rg.handle_getting_data(group)
        if rg.using_admin_token:
            print("Project data retrieval complete. Moving on to User metadata retrieval")
            rg.handle_getting_user_data(group)
        else:
            print("Non-admin token used. Skipping user retrieval")
        print(f"All data retrieval is complete. Writing content to file")
        rg.write_workbook()

@click.command
@click.option("-s", "--source", help="Source URL: REQ'd")
@click.option("-u", "--user", help="Username associated with the Jenkins API token: REQ'd")
@click.option("-t", "--token", help="Jenkins API Token: REQ'd")
def evaluate_jenkins(source, user, token):
    print("NOTE: Jenkins Evaluation is in a BETA state")
    print(f"Connecting to Jenkins instance at {source}")
    r = JKReportGenerator(source, user, token, filename='evaluate_jenkins')
    print("Retrieving Jenkins instance statistics")
    stats = r.get_app_stats()
    print("Retrieving list of Jenkins plugins")
    r.get_plugins()
    print("Retrieving list of Jenkins jobs")
    r.get_raw_data()
    print("Finalizing report")
    r.get_app_stat_extras(stats)
    r.write_workbook()
    print("Report generated. Please review evaluate_jenkins.xlsx")
