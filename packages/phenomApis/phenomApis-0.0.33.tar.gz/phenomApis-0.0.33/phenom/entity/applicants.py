from phenom.api.applicants.applicants_api import ApplicantsApi
from phenom.api.applicants.leads_api import LeadsApi
from phenom.api.applicants.activity_api import ActivityApi
from phenom.api.applicants.hiring_status_api import HiringStatusApi

class Applicants(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    # applicants apis
    def applicants_api(self):
        return ApplicantsApi(self.token, self.gateway_url, self.apikey)

    def activity_api(self):
        return ActivityApi(self.token, self.gateway_url, self.apikey)

    def hiring_status_api(self):
        return HiringStatusApi(self.token, self.gateway_url, self.apikey)

    def leads_api(self):
        return LeadsApi(self.token, self.gateway_url, self.apikey)