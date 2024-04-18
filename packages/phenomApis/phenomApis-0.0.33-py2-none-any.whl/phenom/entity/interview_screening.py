from phenom.api.videoplatform.review_api import ReviewApi
from phenom.api.videoplatform.evaluations_api import EvaluationsApi
from phenom.api.videoplatform.questions_api import QuestionsApi
from phenom.api.videoplatform.candidate_invite_api import CandidateInviteApi
from phenom.api.videoplatform.job_questionnaire_config_api import JobQuestionnaireConfigApi
from phenom.api.videoplatform.questionnaire_templates_api import QuestionnaireTemplatesApi

class InterviewScreening(object):
    def __init__(self, token, gateway_url, apikey=None):
        self.token = token
        self.gateway_url = gateway_url
        self.apikey = apikey

    def review_api(self):
        return ReviewApi(self.token, self.gateway_url, self.apikey)

    def evaluations_api(self):
        return EvaluationsApi(self.token, self.gateway_url, self.apikey)

    def questions_api(self):
        return QuestionsApi(self.token, self.gateway_url, self.apikey)

    def candidate_invite_api(self):
        return CandidateInviteApi(self.token, self.gateway_url, self.apikey)

    def job_questionnaire_config_api(self):
        return JobQuestionnaireConfigApi(self.token, self.gateway_url, self.apikey)

    def questionnaire_templates_api(self):
        return QuestionnaireTemplatesApi(self.token, self.gateway_url, self.apikey)