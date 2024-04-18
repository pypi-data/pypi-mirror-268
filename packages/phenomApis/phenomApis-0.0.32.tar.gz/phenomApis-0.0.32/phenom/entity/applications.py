from phenom.api.apply.attachments_api import AttachmentsApi
from phenom.api.apply.applications_api import ApplicationsApi

class Applications(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    # applications apis
    def attachments_api(self):
        return AttachmentsApi(self.token, self.gateway_url, self.apikey)

    def applications_api(self):
        return ApplicationsApi(self.token, self.gateway_url, self.apikey)