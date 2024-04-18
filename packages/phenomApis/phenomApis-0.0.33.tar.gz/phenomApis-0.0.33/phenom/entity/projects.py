from phenom.api.projects.candidates_api import CandidatesApi
from phenom.api.projects.workflows_api import WorkflowsApi
from phenom.api.projects.projects_api import ProjectsApi
from phenom.api.projects.workflow_status_api import WorkflowStatusApi

class Projects(object):
    def __init__(self, token, gateway_url, apikey):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey
    def candidates_api(self):
        return CandidatesApi(self.token, self.gateway_url, self.apikey)
    def workflows_api(self):
        return WorkflowsApi(self.token, self.gateway_url, self.apikey)
    def projects_api(self):
        return ProjectsApi(self.token, self.gateway_url, self.apikey)
    def workflow_status_api(self):
        return WorkflowStatusApi(self.token, self.gateway_url, self.apikey)
