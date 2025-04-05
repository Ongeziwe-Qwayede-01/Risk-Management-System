stateDiagram-v2
    [*] --> Identified
    Identified --> Assessed : Risk Assessment Completed
    Assessed --> Mitigated : Mitigation Plan Approved
    Assessed --> Assigned : Assigned to Risk Owner
    Mitigated --> Reviewed : Review Submitted
    Reviewed --> Closed : Approved by Risk Manager
    Assessed --> Rejected : Not Accepted
    Closed --> Archived : Audit Logged
