import jenkins
from dacite import from_dict
from gitlab_evaluate.migration_readiness.jenkins.data_classes.plugin import JenkinsPlugin

class JenkinsEvaluateClient():
    def __init__(self, host, user, token) -> None:
        self.server = jenkins.Jenkins(host, username=user, password=token)
        self.user = self.server.get_whoami()
        self.version = self.server.get_version()
        self.plugins = self.server.get_plugins_info()
        self.num_jobs = self.server.jobs_count()
        self.job_types = []
    
    def list_of_plugins(self):
        for plugin in self.plugins:
            yield from_dict(JenkinsPlugin, plugin)

    def list_of_jobs(self):
        for job in self.server.get_jobs():
            if job['_class'] not in self.job_types:
                self.job_types.append(job['_class'])
            yield job

    