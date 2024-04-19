import xlsxwriter
from gitlab_ps_utils.json_utils import json_pretty
from gitlab_ps_utils.processes import MultiProcessing
from gitlab_evaluate.lib import utils
from gitlab_evaluate.migration_readiness.jenkins.evaluate import JenkinsEvaluateClient
from gitlab_evaluate.migration_readiness.jenkins.data_classes.plugin import JenkinsPlugin


class ReportGenerator():
    def __init__(self, host, user, token, filename=None, output_to_screen=False, evaluate_api=None, processes=None):
        self.host = host
        self.jenkins_client = JenkinsEvaluateClient(host, user, token)
        if filename:
            self.workbook = xlsxwriter.Workbook(f'{filename}.xlsx')
        else:
            self.workbook = xlsxwriter.Workbook('evaluate_report.xlsx')
        self.app_stats = self.workbook.add_worksheet('App Stats')
        self.align_left = self.workbook.add_format({'align': 'left'})
        # Create Header format with a black background
        self.header_format = self.workbook.add_format({'bg_color': 'black', 'font_color': 'white', 'bold': True, 'font_size': 10})
        self.workbook.add_format({'text_wrap': True, 'font_size': 10})
        self.plugins = self.workbook.add_worksheet('Plugins')
        self.raw_output = self.workbook.add_worksheet('Raw Job Data')
        self.output_to_screen = output_to_screen
        self.multi = MultiProcessing()
        self.processes = processes
        self.csv_columns = [
            'fullname',
            'name',
            'url',
            'color',
            '_class'
        ]
        self.plugin_columns = list(JenkinsPlugin.__annotations__.keys())
        
        utils.write_headers(0, self.raw_output, self.csv_columns, self.header_format)
        utils.write_headers(0, self.plugins, self.plugin_columns, self.header_format)

    def write_workbook(self):
        self.app_stats.autofit()
        self.raw_output.autofit()
        self.plugins.autofit()
        self.workbook.close()

    def get_app_stats(self):
        '''
            Gets Jenkins instance stats
        '''
        report_stats = []
        report_stats += [
            ('Basic information from source', self.host),
            ('Customer', '<CUSTOMERNAME>'),
            ('Date Run', utils.get_date_run()),
            ('Source', 'Jenkins'),
            ('Jenkins Version', self.jenkins_client.server.get_version()),
            ('Total Jobs', self.jenkins_client.num_jobs),
            ('Total Plugins Installed', len(self.jenkins_client.plugins))
        ]
        for row, stat in enumerate(report_stats):
            self.app_stats.write(row, 0, stat[0])
            self.app_stats.write(row, 1, stat[1])
        return report_stats
    
    def get_app_stat_extras(self, report_stats):
        '''
            Writes a series of rows with formulas to other sheets to get additional counts
        '''
        additional_stats = [
            ('Total Plugins Needing an Update', f"={utils.get_countif(self.plugins.get_name(), 'True', 'E')}"),
            ('Total Plugins Enabled', f"={utils.get_countif(self.plugins.get_name(), 'True', 'F')}")
        ]
        for job_type in self.jenkins_client.job_types:
            additional_stats.append(
                (f"Total '{job_type}' jobs", f"={utils.get_countif(self.raw_output.get_name(), job_type, 'E')}")
            )
        starting_point = len(report_stats)
        for row, stat in enumerate(additional_stats):
            self.app_stats.write(row+starting_point, 0, stat[0])
            self.app_stats.write(row+starting_point, 1, stat[1])
    
    def get_plugins(self):
        """
            Gets a list of plugins and writes the data to the 'Plugins' sheet
        """
        for row, plugin in enumerate(self.jenkins_client.list_of_plugins()):
            for col, col_name in enumerate(self.plugin_columns):
                self.plugins.write(row+1, col, getattr(plugin, col_name))

    def get_raw_data(self):
        '''
            Retrieves a list of Jenkins Jobs and writes all the data to the 'Raw Job Data' sheet
        '''
        for row, job in enumerate(self.jenkins_client.list_of_jobs()):
            for col, col_name in enumerate(self.csv_columns):
                self.raw_output.write(row+1, col, job[col_name])

    def write_output_to_files(self, flags, messages, results):
        dict_data = []
        dict_data.append({x: results.get(x) for x in self.csv_columns})
        utils.append_to_workbook(self.raw_output, dict_data, self.csv_columns)

        if True in flags:
            utils.append_to_workbook(
                self.flagged_projects, dict_data, self.csv_columns)
            utils.append_to_workbook(self.final_report, [{'Project': results.get(
                'Project'), 'Reason': messages.generate_report_entry()}], self.report_headers)
        if self.output_to_screen:
            print(f"""
            {'+' * 40}
            {json_pretty(results)}
            """)

