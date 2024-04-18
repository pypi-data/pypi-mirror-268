from phenom.api.evaluation.interview_evaluations_api import InterviewEvaluationsApi
from phenom.api.evaluation.jobs_api import JobsApi

class Evaluations(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey
    def interview_evaluations_api(self):
        return InterviewEvaluationsApi(self.token, self.gateway_url, self.apikey)

    def jobs_api(self):
        return JobsApi(self.token, self.gateway_url, self.apikey)