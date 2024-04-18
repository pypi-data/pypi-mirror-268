from phenom.api.candidatesactivities.notes_api import NotesApi

class Candidate(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    def notes_api(self):
        return NotesApi(self.token, self.gateway_url, self.apikey)