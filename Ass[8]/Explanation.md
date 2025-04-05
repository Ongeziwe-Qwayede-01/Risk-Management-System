📄 Object State Model Explanations – Risk Management System (RMS)
This document summarizes the purpose, key transitions, and functional relevance of the eight critical objects modeled in the state transition diagrams. Each explanation ties directly into your RMS system’s functional requirements and user stories for traceability and design alignment.

1. 🛡️ Risk Object
Explanation:
Represents the full lifecycle of a risk in the system. It begins with identification and transitions through assessment, approval, mitigation, and monitoring, eventually reaching closure and archiving. This flow supports traceable and well-managed risk handling.

Linked Functional Requirement: FR-001 – Identify and Assess Risks

User Stories: Identify Risks, Assign Risks, Monitor Risks

2. 📝 Mitigation Plan
Explanation:
Tracks the evolution of a mitigation strategy designed to respond to an identified risk. It begins as a draft, moves through submission, and can either be approved or rejected. Approved plans are then implemented, verified, and ultimately closed and archived.

Linked Functional Requirement: FR-002 – Approve Mitigation Plans

User Stories: Approve Mitigation Plans, Assign Tasks

3. 👤 User Account
Explanation:
Outlines the different states of a user's account within the RMS. After registration, an account is activated once verified. It may be suspended due to issues or deactivated upon request. Closed accounts are archived for record-keeping.

Linked Functional Requirement: FR-006 – Manage User Roles and Permissions

User Stories: Manage Roles, Support Concurrent Users

4. 📊 Risk Report
Explanation:
Describes how a risk report moves from being generated to reviewed, approved, and then distributed to stakeholders. Finally, reports are archived to satisfy compliance and historical analysis.

Linked Functional Requirement: FR-003 – Review Risk Reports

User Stories: Review Reports, Generate Compliance Reports

5. 📄 Compliance Report
Explanation:
Used to ensure adherence to regulatory standards. Compliance reports are created, then validated by auditors. They are either submitted and accepted, or rejected and revised. Accepted reports are archived for compliance purposes.

Linked Functional Requirement: FR-008 – Generate Compliance Reports

User Stories: Generate Compliance Reports

6. 🚨 Alert
Explanation:
Models how the system handles real-time alerts. An alert is triggered, then sent to relevant users. Once acknowledged, it is either resolved or escalated further based on actions taken.

Linked Functional Requirement: FR-005 – Generate Real-Time Alerts

User Stories: Generate Alerts, Link Risks to Incidents

7. 📜 Audit Log
Explanation:
Captures and maintains logs of system events. The log starts when initiated, continues while logging, and ends with finalization and archiving. This ensures accountability and transparency in system activities.

Linked Functional Requirement: FR-010 – Log Risk Actions for Audit

User Stories: Log Actions, Manage History

8. 💾 Backup Job
Explanation:
Manages automated backup processes. Begins as scheduled, then runs, either succeeds or fails. Failed jobs may be retried. Successful backups are verified and archived, ensuring data integrity and disaster recovery capability.

Linked Functional Requirement: FR-011 – Automated Data Backups

User Stories: Backup System, Handle Failures
