from phenom.api.tags.tags_api import TagsApi
from phenom.api.tags.candidates_api import CandidatesApi

class Tags(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    def tags_api(self):
        return TagsApi(self.token, self.gateway_url, self.apikey)

    def candidates_api(self):
        return CandidatesApi(self.token, self.gateway_url, self.apikey)