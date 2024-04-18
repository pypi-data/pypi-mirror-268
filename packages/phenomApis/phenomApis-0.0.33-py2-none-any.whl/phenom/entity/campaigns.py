from phenom.api.campaignssms.sms_campaigns_api import SMSCampaignsApi
from phenom.api.campaignsemail.email_campaigns_api import EmailCampaignsApi

class Campaigns:
    def __init__(self, token, gateway_url, apikey):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    def sms_campaigns_api(self):
        return SMSCampaignsApi(self.token, self.gateway_url, self.apikey)

    def email_campaigns_api(self):
        return EmailCampaignsApi(self.token, self.gateway_url, self.apikey)