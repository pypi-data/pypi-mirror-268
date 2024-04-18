from phenom.api.servicehubpublic.user_management_api import UserManagementApi
from phenom.api.servicehubscim.scim_api import SCIMApi

class UserManagement(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    def user_management(self):
        return UserManagementApi(self.token, self.gateway_url, self.apikey)

    def scim_api(self):
        return SCIMApi(self.token, self.gateway_url, self.apikey)