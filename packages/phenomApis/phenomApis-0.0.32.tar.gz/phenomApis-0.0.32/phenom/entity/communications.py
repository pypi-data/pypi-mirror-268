from phenom.api.communicationssms.sms_communications_api import SMSCommunicationsApi
from phenom.api.communicationsemail.email_communications_api import EmailCommunicationsApi
from phenom.api.communicationsemail.forward_profile_api import ForwardProfileApi

class Communications(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    def sms_communications_api(self):
        return SMSCommunicationsApi(self.token, self.gateway_url, self.apikey)

    def email_communications_api(self):
        return EmailCommunicationsApi(self.token, self.gateway_url, self.apikey)

    def forward_profile_api(self):
        return ForwardProfileApi(self.token, self.gateway_url, self.apikey)