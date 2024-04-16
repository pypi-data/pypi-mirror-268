from phenom.api.jobsync.jobs_api import JobsApi
from phenom.api.jobactivities.job_category_api import JobCategoryApi
from phenom.api.jobactivities.job_attachments_api import JobAttachmentsApi
from phenom.api.jobactivities.job_notes_api import JobNotesApi
from phenom.api.jobactivities.hiring_team_api import HiringTeamApi
from phenom.api.jobquestionnarie.job_questionnaire_api import JobQuestionnaireApi
from phenom.api.jobquestionnarie.questionnaire_templates_api import QuestionnaireTemplatesApi
class Jobs(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey
    def jobs(self):
        return JobsApi(self.token, self.gateway_url, self.apikey)
        # job activities apis

    def hiring_team(self):
        return HiringTeamApi(self.token, self.gateway_url, self.apikey)

    def job_attachments(self):
        return JobAttachmentsApi(self.token, self.gateway_url, self.apikey)

    def job_category(self):
        return JobCategoryApi(self.token, self.gateway_url, self.apikey)

    def job_notes(self):
        return JobNotesApi(self.token, self.gateway_url, self.apikey)

        # job questionnaire apis

    def job_questionnaire(self):
        return JobQuestionnaireApi(self.token, self.gateway_url, self.apikey)

    def job_questionnaire_templates(self):
        return QuestionnaireTemplatesApi(self.token, self.gateway_url, self.apikey)
