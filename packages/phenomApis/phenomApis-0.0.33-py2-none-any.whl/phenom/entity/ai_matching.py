from phenom.api.aisourcing.ai_matching_api import AIMatchingApi


class AIMatching(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    # ai-sourcing apis
    def ai_matching_api(self):
        return AIMatchingApi(self.token, self.gateway_url, self.apikey)