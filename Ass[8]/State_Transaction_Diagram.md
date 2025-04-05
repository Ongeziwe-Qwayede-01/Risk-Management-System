1. 🛡️ Risk Object
mermaid
Copy
Edit
stateDiagram-v2
    [*] --> Identified
    Identified --> Assessed : Risk Assessment Completed
    Assessed --> Approved : Approved by Committee
    Approved --> Mitigated : Mitigation Started
    Mitigated --> Monitored : Risk Under Observation
    Monitored --> Closed : Risk Resolved
    Closed --> Archived : Record Retention
Explanation:
Represents the full lifecycle of a risk in the system. It begins with identification and goes through assessment, approval, mitigation, and monitoring before closure and archiving.

Linked Functional Requirement: FR-001 (Identify and Assess Risks)

User Stories: Identify Risks, Assign Risks, Monitor Risks

2. 📝 Mitigation Plan
mermaid
Copy
Edit
stateDiagram-v2
    [*] --> Draft
    Draft --> Submitted : Submitted for Approval
    Submitted --> Approved : Approved by Risk Committee
    Submitted --> Rejected : Not Accepted
    Approved --> Implemented : Implementation Started
    Implemented --> Verified : QA/Testing Passed
    Verified --> Closed : Final Review Passed
    Closed --> Archived : Audit Logged
Explanation:
Tracks the evolution of a risk mitigation plan, from drafting and submission to implementation and closure. This ensures formal review and testing before final archiving.

Linked Requirement: FR-002 (Approve Mitigation Plans)

User Stories: Approve Mitigation Plans, Assign Tasks

3. 👤 User Account
mermaid
Copy
Edit
stateDiagram-v2
    [*] --> Registered
    Registered --> Active : Email Verified
    Active --> Suspended : Admin Action
    Suspended --> Reactivated : Issue Resolved
    Active --> Deactivated : Voluntary Closure
    Deactivated --> Archived : Data Retention
Explanation:
Outlines the lifecycle of a system user account, including states like registration, activation, suspension, and deactivation. Supports user management and access control.

Linked Requirement: FR-006 (Manage User Roles and Permissions)

User Stories: Manage Roles, Support Concurrent Users

4. 📊 Risk Report
mermaid
Copy
Edit
stateDiagram-v2
    [*] --> Generated
    Generated --> UnderReview : Sent to Reviewer
    UnderReview --> Approved : Report Accepted
    Approved --> Distributed : Sent to Stakeholders
    Distributed --> Archived : Compliance Storage
Explanation:
Covers generation, review, and final distribution of reports. Critical for decision-making and compliance tracking.

Linked Requirement: FR-003 (Review Risk Reports)

User Stories: Review Reports, Generate Compliance Reports

5. 📄 Compliance Report
mermaid
Copy
Edit
stateDiagram-v2
    [*] --> Created
    Created --> Validated : Auditor Review
    Validated --> Submitted : Sent to Regulator
    Submitted --> Accepted : Approved by Authority
    Submitted --> Rejected : Returned for Edits
    Accepted --> Archived : Long-Term Storage
Explanation:
Used for regulatory compliance. Includes submission to external bodies and handling of rejection cases.

Linked Requirement: FR-008 (Generate Compliance Reports)

User Stories: Generate Compliance Reports

6. 🚨 Alert
mermaid
Copy
Edit
stateDiagram-v2
    [*] --> Triggered
    Triggered --> Sent : System Notifies User
    Sent --> Acknowledged : User Reads Alert
    Acknowledged --> Resolved : Action Taken
Explanation:
Models real-time risk alerting and resolution. Ensures timely stakeholder notification and action.

Linked Requirement: FR-005 (Generate Real-Time Alerts)

User Stories: Generate Alerts, Link Risks to Incidents

7. 📜 Audit Log
mermaid
Copy
Edit
stateDiagram-v2
    [*] --> Initiated
    Initiated --> Logging : Recording Actions
    Logging --> Finalized : Session Ended
    Finalized --> Archived : Compliance Storage
Explanation:
Tracks user/system actions for traceability. Supports audits and legal accountability.

Linked Requirement: FR-010 (Log Risk Actions for Audit)

User Stories: Log Actions, Manage History

8. 💾 Backup Job
mermaid
Copy
Edit
stateDiagram-v2
    [*] --> Scheduled
    Scheduled --> Running : Job Started
    Running --> Successful : Data Saved
    Running --> Failed : Error Occurred
    Failed --> Retried : Retry Initiated
    Successful --> Verified : Check Passed
    Verified --> Archived : Stored Securely
Explanation:
Handles automated backup processes, including retries and verification. Ensures data integrity and disaster recovery readiness.

Linked Requirement: FR-011 (Automated Data Backups)

User Stories: Backup System, Handle Failures
