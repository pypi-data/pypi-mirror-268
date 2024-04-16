import json
import requests
from ..constants import *
from .helper import JsonHelper, JiraFieldsHelper


class IssueJira:

    def get_issue(self, issue_key, debug=False):
        issue = self._get_issue_data(issue_key)
        JsonHelper().save_json(f'Issue_{issue_key}',issue) if debug else None

        return issue
    
    def get_issue_fields_data(self, issue_key, debug=False):

        issue = self._get_issue_data(issue_key)
        issue_fields = self._get_issue_fields(issue)
        
        JsonHelper().save_json(f'Issue_Fields_{issue_key}',issue_fields) if debug else None
        issue_fields_min = JiraFieldsHelper().remove_null_fields(issue_fields)

        return issue_fields_min

    def _get_issue_data(self, issue_key):
        try:
            request = requests.get(
                f"{API_ISSUE_URL}/issue/{issue_key}",
                # f"{API_ISSUE_URL}/{CLOUD_ID}/issue/{issue_key}",
                headers=API_HEADERS,
                auth=JIRA_AUTH,
            )
            request.raise_for_status()
            data = request.json()

            return data
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Erro ao receber formulario da issue:\n{e}")
        
    def _get_issue_fields(self, issue):

        jira_fields = issue.get('fields')
        return jira_fields
    

        
class AttachmentJira:

    def get_attachment(self, issue):

        self._check_issue_attachment(issue)
        attachments_ids = self._get_attachment_id(issue)
        attachment = {}
        for attachment_key in attachments_ids:
            attachments_from_issue = self._get_attachments_from_issue(attachment_key)
            if attachments_from_issue:
                attachment = attachments_from_issue

        
        return attachment
        
    def _check_issue_attachment(self, issue):
        if issue.get("fields")["attachment"] is None:
            raise Exception("Could not find attachment")
        
    def _get_attachments_from_issue(self, attachment_key):
        try:
            request = requests.get(
                f"{API_ISSUE_URL}/attachment/content/{attachment_key}",
                headers=API_ATTACHMENT_HEADERS,
                auth=JIRA_AUTH,
            )
            request.raise_for_status()
            check_pdf = self._check_pdf_attachment(request)
            attachment_data = request.json() if not check_pdf else None

            return attachment_data

        except requests.exceptions.HTTPError as e:
            raise Exception(f"Erro ao receber anexo Jira:\n{e}")
        
    def _check_pdf_attachment(self, request):
        check_pdf = True if "application/pdf" in request.headers.get("Content-Type", "") else False
        return check_pdf
    
    def _get_attachment_id(self, issue):
        attachment_ids = []

        for attachment in issue.get("fields")["attachment"]:
            attachment_ids.append(attachment["id"])

        return attachment_ids
    
class TransitionJira:

    def post_transition(self, transition_id, issue_key):

        self._post_transition(transition_id, issue_key)
        pass

    def _post_transition(self, transition_id, issue_key):

        payload = json.dumps(
            {
                "transition": {"id": transition_id},
                "update": {"comment": []},
            }
        )
        try:
            res = requests.post(
                f"{API_ISSUE_URL}/issue/{issue_key}/transitions",
                auth=JIRA_AUTH,
                headers=API_HEADERS,
                data=payload,
            )
            res.raise_for_status()
            pass
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Erro ao receber formulario da issue:\n{e}")    