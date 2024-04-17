import json
from dataclasses import asdict, dataclass

import pandas as pd

import config
from synch2jira.issue_workflow_json import IssueWorkflowJSON


@dataclass
class IssueJSON():
    issue_key: str
    issue_id: str
    statuscategorychangedate: str
    issuetypeid: str
    issuetypedescription: str
    issuetypename: str
    issuetypesubtask: bool
    issuetypehierarchyLevel: str
    timespend: str
    projectid: str
    projectkey: str
    projectname: str
    projectTypeKey: str
    aggregatetimespent: str
    # resolution : str
    resolutiondate: str
    workratio: str
    watchCount: str
    isWatching: bool
    lastViewed: str
    created: str
    priorityname: str
    priorityid: str
    labelsnumber: str
    assignee: str
    updated: str
    statusname: str
    statuscategoryname: str
    timeoriginalestimate: str
    description: str
    security: str
    aggregatetimeestimate: str
    summary: str
    creatoremailAddress: str
    creatorname: str
    subtasksnumber: str
    reportername: str
    reporteremail: str
    duedate: str
    votes: str
    workflow_start_time: str
    workflow_end_time: str

    @staticmethod
    def json_to_issue(issue_data, json_data, state1, state2):
        fields = issue_data.get("fields", {})
        issue_key = issue_data.get("key")
        priority = fields.get("priority") or {}
        creator_data = fields["creator"] or {}
        assignee_data = fields["assignee"] or {}
        security_data = fields["security"] or {}
        workflow_start_time, workflow_end_time = IssueWorkflowJSON.get_lead_time(json_data, issue_key, state1, state2)
        return IssueJSON(
            issue_key=issue_data.get("key"),
            issue_id=issue_data.get("id"),
            statuscategorychangedate=fields.get("statuscategorychangedate"),
            issuetypeid=fields["issuetype"].get("id"),
            issuetypedescription=fields["issuetype"].get("description"),
            issuetypename=fields["issuetype"].get("name"),
            issuetypesubtask=fields["issuetype"].get("subtask"),
            issuetypehierarchyLevel=fields["issuetype"].get("hierarchyLevel"),
            timespend=fields.get("timespent"),
            projectid=fields["project"].get("id"),
            projectkey=fields["project"].get("key"),
            projectname=fields["project"].get("name"),
            projectTypeKey=fields["project"].get("projectTypeKey"),
            aggregatetimespent=fields.get("aggregatetimespent"),
            # resolution=fields.get("resolution"),
            resolutiondate=fields.get("resolutiondate"),
            workratio=fields.get("workratio"),
            watchCount=fields["watches"].get("watchCount"),
            isWatching=fields["watches"].get("isWatching"),
            lastViewed=fields.get("lastViewed"),
            created=fields["created"].replace(" ", ""),
            priorityname=priority.get("name"),
            priorityid=priority.get("id"),
            labelsnumber=len(fields.get("labels", [])),
            assignee=assignee_data.get("displayName"),
            updated=fields["updated"].replace(" ", ""),
            statusname=fields["status"].get("name"),
            statuscategoryname=fields["status"]["statusCategory"].get("name"),
            timeoriginalestimate=fields.get("timeoriginalestimate"),
            description="",
            # description=fields["description"]["content"][0].get("text"),
            security=security_data.get("description"),
            aggregatetimeestimate=fields.get("aggregatetimeestimate"),
            summary=fields.get("summary"),
            creatoremailAddress=creator_data.get("emailAddress"),
            creatorname=creator_data.get("displayName"),
            subtasksnumber=len(fields.get("subtasks", [])),
            reportername=fields["reporter"].get("displayName"),
            reporteremail=fields["reporter"].get("emailAddress"),
            duedate=fields.get("duedate", ""),
            votes=fields["votes"].get("votes"),
            workflow_start_time=workflow_start_time,
            workflow_end_time=workflow_end_time

        )

    def json_to_data_frame(file_data=config.json_issues_file):
        with open(file_data, 'r') as file:
            json_data = json.load(file)
        issue_list = [IssueJSON.json_to_issue(issue_data, json_data, config.workflow_status1,
                                                            config.workflow_status2) for issue_data in json_data]
        data = [asdict(issue_json) for issue_json in issue_list]
        dataframe = pd.DataFrame(data)
        return dataframe
