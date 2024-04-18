from phenom.api.employees.employee_profile_api import EmployeeProfileApi
from phenom.api.employees.employee_preferences_api import EmployeePreferencesApi
from phenom.api.employeescourses.employee_courses_api import EmployeeCoursesApi
from phenom.api.employeesreferral.employee_referrals_api import EmployeeReferralsApi
from phenom.api.employeescareerpath.employee_career_path_api import EmployeeCareerPathApi

from phenom.api.exsearch.employee_search_api import EmployeeSearchApi
from phenom.api.exsearch.mentor_api import MentorApi

class Employees(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    def employee_profile_api(self):
        return EmployeeProfileApi(self.token, self.gateway_url, self.apikey)

    def employee_preferences_api(self):
        return EmployeePreferencesApi(self.token, self.gateway_url, self.apikey)

    def employee_courses_api(self):
        return EmployeeCoursesApi(self.token, self.gateway_url, self.apikey)

    def employee_referrals_api(self):
        return EmployeeReferralsApi(self.token, self.gateway_url, self.apikey)

    def employee_career_path_api(self):
        return EmployeeCareerPathApi(self.token, self.gateway_url, self.apikey)

    def employee_search_api(self):
        return EmployeeSearchApi(self.token, self.gateway_url, self.apikey)

    def mentor_api(self):
        return MentorApi(self.token, self.gateway_url, self.apikey)