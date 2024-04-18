from phenom.api.prediction.prediction_api import PredictionApi

class Prediction(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    def prediction_api(self):
        return PredictionApi(self.token, self.gateway_url, self.apikey)