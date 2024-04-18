from phenom.api.resumeparser.resume_parsing_api import ResumeParsingApi
from phenom.api.jobparser.job_parsing_api import JobParsingApi

class Parsers(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    # resumeparser apis
    def resume_parsing_api(self):
        return ResumeParsingApi(self.token, self.gateway_url, self.apikey)
    # job-parser apis
    def job_parsing_api(self):
        return JobParsingApi(self.token, self.gateway_url, self.apikey)