from phenom.api.candidatesactivities.notes_api import NotesApi

class Candidate(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.__token = token
        self.__gateway_url = gateway_url
        self.__apikey = apikey

    def notes_api(self):
        return NotesApi(self.__token, self.__gateway_url, self.__apikey)