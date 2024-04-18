from phenom.api.hrm.jobs_api import JobsApi

class HiringManager(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey
    def jobs_api(self):
        return JobsApi(self.token, self.gateway_url, self.apikey)