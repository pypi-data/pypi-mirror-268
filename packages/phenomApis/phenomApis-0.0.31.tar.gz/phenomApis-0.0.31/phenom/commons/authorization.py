from phenom.commons.get_token import tokengeneration

from phenom.api.resumeparser.resume_parsing_api import ResumeParsingApi
from phenom.api.exsearch.employee_search_api import EmployeeSearchApi
from phenom.api.exsearch.mentor_api import MentorApi
from phenom.api.prediction.prediction_api import PredictionApi
from phenom.api.aisourcing.ai_matching_api import AIMatchingApi
from phenom.api.search.search_api import SearchApi
from phenom.api.jobparser.job_parsing_api import JobParsingApi
from phenom.api.recommendation.recommendations_api import RecommendationsApi

from phenom.api.applicants.applicants_api import ApplicantsApi
from phenom.api.applicants.leads_api import LeadsApi
from phenom.api.applicants.activity_api import ActivityApi
from phenom.api.applicants.hiring_status_api import HiringStatusApi
from phenom.api.jobactivities.job_category_api import JobCategoryApi
from phenom.api.jobactivities.job_attachments_api import JobAttachmentsApi
from phenom.api.jobactivities.job_notes_api import JobNotesApi
from phenom.api.jobactivities.hiring_team_api import HiringTeamApi
from phenom.api.jobquestionnarie.job_questionnaire_api import JobQuestionnaireApi
from phenom.api.jobquestionnarie.questionnaire_templates_api import QuestionnaireTemplatesApi
from phenom.api.projects.candidates_api import CandidatesApi as projectsCandidatesApi
from phenom.api.projects.workflows_api import WorkflowsApi
from phenom.api.projects.projects_api import ProjectsApi
from phenom.api.projects.workflow_status_api import WorkflowStatusApi
from phenom.api.tags.tags_api import TagsApi
from phenom.api.tags.candidates_api import CandidatesApi as tagsCandidatesApi

from phenom.api.campaignssms.sms_campaigns_api import SMSCampaignsApi
from phenom.api.campaignsemail.email_campaigns_api import EmailCampaignsApi
from phenom.api.communicationssms.sms_communications_api import SMSCommunicationsApi
from phenom.api.communicationsemail.email_communications_api import EmailCommunicationsApi
from phenom.api.communicationsemail.forward_profile_api import ForwardProfileApi

from phenom.api.servicehubpublic.user_management_api import UserManagementApi
from phenom.api.servicehubscim.scim_api import SCIMApi
from phenom.commons.parsers import Parsers
from phenom.api.candidatesactivities.notes_api import NotesApi

from phenom.api.jobsync.jobs_api import JobsApi

from phenom.api.employees.employee_profile_api import EmployeeProfileApi
from phenom.api.employees.employee_preferences_api import EmployeePreferencesApi
from phenom.api.employeescourses.employee_courses_api import EmployeeCoursesApi
from phenom.api.employeesreferral.employee_referrals_api import EmployeeReferralsApi
from phenom.api.employeescareerpath.employee_career_path_api import EmployeeCareerPathApi

from phenom.api.apply.attachments_api import AttachmentsApi
from phenom.api.apply.applications_api import ApplicationsApi

from phenom.api.videoplatform.review_api import ReviewApi
from phenom.api.videoplatform.evaluations_api import EvaluationsApi
from phenom.api.videoplatform.questions_api import QuestionsApi
from phenom.api.videoplatform.candidate_invite_api import CandidateInviteApi
from phenom.api.videoplatform.job_questionnaire_config_api import JobQuestionnaireConfigApi
from phenom.api.videoplatform.questionnaire_templates_api import \
    QuestionnaireTemplatesApi as VxQuestionnaireTemplatesApi

from phenom.api.evaluation.interview_evaluations_api import InterviewEvaluationsApi
from phenom.api.evaluation.jobs_api import JobsApi as EvaluationJobsApi
from phenom.api.hrm.jobs_api import JobsApi as HrmJobsApi

from phenom.commons.jobs import Jobs

class Authorization(object):
    def __init__(self, url, client_id, client_secret, gateway_url, apikey=None):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.gateway_url = gateway_url
        self.apikey = apikey
    def parsers(self):
        return Parsers(self.token(), self.gateway_url, self.apikey)
    def jobs(self):
        return Jobs(self.token(), self.gateway_url, self.apikey)
    def token(self):
        return tokengeneration(self.url, self.client_id, self.client_secret)

    # resumeparser apis
    def resume_parsing(self):
        return ResumeParsingApi(self.token(), self.gateway_url, self.apikey)

    # employee search apis
    def employee_search(self):
        return EmployeeSearchApi(self.token(), self.gateway_url, self.apikey)

    def mentor(self):
        return MentorApi(self.token(), self.gateway_url, self.apikey)

    # prediction apis
    def prediction(self):
        return PredictionApi(self.token(), self.gateway_url, self.apikey)

    # ai-sourcing apis
    def ai_sourcing(self):
        return AIMatchingApi(self.token(), self.gateway_url, self.apikey)

    # search apis
    def search(self):
        return SearchApi(self.token(), self.gateway_url, self.apikey)

    # job-parser apis
    def job_parser(self):
        return JobParsingApi(self.token(), self.gateway_url, self.apikey)

    # recommendation apis
    def recommendation(self):
        return RecommendationsApi(self.token(), self.gateway_url, self.apikey)

    # applicants apis
    def applicants(self):
        return ApplicantsApi(self.token(), self.gateway_url, self.apikey)

    def activity(self):
        return ActivityApi(self.token(), self.gateway_url, self.apikey)

    def hiring_status(self):
        return HiringStatusApi(self.token(), self.gateway_url, self.apikey)

    def leads(self):
        return LeadsApi(self.token(), self.gateway_url, self.apikey)

    # job activities apis
    def hiring_team(self):
        return HiringTeamApi(self.token(), self.gateway_url, self.apikey)

    def job_attachments(self):
        return JobAttachmentsApi(self.token(), self.gateway_url, self.apikey)

    def job_category(self):
        return JobCategoryApi(self.token(), self.gateway_url, self.apikey)

    def job_notes(self):
        return JobNotesApi(self.token(), self.gateway_url, self.apikey)

    # job questionnaire apis
    def job_questionnaire(self):
        return JobQuestionnaireApi(self.token(), self.gateway_url, self.apikey)

    def job_questionnaire_templates(self):
        return QuestionnaireTemplatesApi(self.token(), self.gateway_url, self.apikey)

    # projects apis
    def projects_candidates(self):
        return projectsCandidatesApi(self.token(), self.gateway_url, self.apikey)

    def projects(self):
        return ProjectsApi(self.token(), self.gateway_url, self.apikey)

    def workflow_status(self):
        return WorkflowStatusApi(self.token(), self.gateway_url, self.apikey)

    def workflows(self):
        return WorkflowsApi(self.token(), self.gateway_url, self.apikey)

    # tags apis
    def tags_candidates(self):
        return tagsCandidatesApi(self.token(), self.gateway_url, self.apikey)

    def tags(self):
        return TagsApi(self.token(), self.gateway_url, self.apikey)

    # crm messaging apis
    def email_campaigns(self):
        return EmailCampaignsApi(self.token(), self.gateway_url, self.apikey)

    def sms_campaigns(self):
        return SMSCampaignsApi(self.token(), self.gateway_url, self.apikey)

    def email_communications(self):
        return EmailCommunicationsApi(self.token(), self.gateway_url, self.apikey)

    def forward_profile(self):
        return ForwardProfileApi(self.token(), self.gateway_url, self.apikey)

    def sms_communications(self):
        return SMSCommunicationsApi(self.token(), self.gateway_url, self.apikey)

    # service hub apis
    def user_management(self):
        return UserManagementApi(self.token(), self.gateway_url, self.apikey)

    def scim_api(self):
        return SCIMApi(self.token(), self.gateway_url, self.apikey)

    # candidates activities apis
    def notes_api(self):
        return NotesApi(self.token(), self.gateway_url, self.apikey)

    # job sync apis
    def jobs_api(self):
        return JobsApi(self.token(), self.gateway_url, self.apikey)

    # im apis
    def employee_profile(self):
        return EmployeeProfileApi(self.token(), self.gateway_url, self.apikey)

    def employee_careerpath(self):
        return EmployeeCareerPathApi(self.token(), self.gateway_url, self.apikey)

    def employee_courses(self):
        return EmployeeCoursesApi(self.token(), self.gateway_url, self.apikey)

    def employee_referrals(self):
        return EmployeeReferralsApi(self.token(), self.gateway_url, self.apikey)

    def employee_preferences(self):
        return EmployeePreferencesApi(self.token(), self.gateway_url, self.apikey)

    # apply apis
    def attachments(self):
        return AttachmentsApi(self.token(), self.gateway_url, self.apikey)

    def applications(self):
        return ApplicationsApi(self.token(), self.gateway_url, self.apikey)

    # video platform apis
    def review(self):
        return ReviewApi(self.token(), self.gateway_url, self.apikey)

    def question(self):
        return QuestionsApi(self.token(), self.gateway_url, self.apikey)

    def evaluations(self):
        return EvaluationsApi(self.token(), self.gateway_url, self.apikey)

    def candidate_invite(self):
        return CandidateInviteApi(self.token(), self.gateway_url, self.apikey)

    def job_questionnaire_config(self):
        return JobQuestionnaireConfigApi(self.token(), self.gateway_url, self.apikey)

    def vx_questionnaire_templates(self):
        return VxQuestionnaireTemplatesApi(self.token(), self.gateway_url, self.apikey)

    # hrm apis
    def interview_evaluations(self):
        return InterviewEvaluationsApi(self.token(), self.gateway_url, self.apikey)

    def evaluations_jobs(self):
        return EvaluationJobsApi(self.token(), self.gateway_url, self.apikey)

    def hrm_jobs(self):
        return HrmJobsApi(self.token(), self.gateway_url, self.apikey)
