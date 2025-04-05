## Activity Diagram Explanations – Risk Management System (RMS)

This document provides clear, concise descriptions of key activity workflows in the RMS. Each section outlines the actors involved, the linked functional requirements, relevant user stories, and a plain-language explanation of the workflow.

**1. Identify and Assess Risks**

- Actors: Risk Manager, System
- Linked FR: FR-001 (Identify and Assess Risks)
- User Stories: Identify Risks, Assign Risks

**Explanation** :This workflow captures the process of risk identification and evaluation. It enables proactive planning by allowing users to input, validate, and assess risk entries.

2. Approve Mitigation Plans

- Actors: Team Lead, System
- Linked FR: FR-002 (Approve Mitigation Plans)
- User Stories: Approve Plans, Assign Tasks

**Explanation**:This process models how a mitigation plan moves through submission, review, optional revision, and final approval. It ensures mitigation is peer-reviewed and actionable.

3. Review Risk Reports

Actors: Analyst, SystemLinked FR: FR-003 (Review Risk Reports)User Stories: Review Reports

Explanation:This workflow ensures that reports are reviewed by an analyst, verified for completeness, and published for stakeholder access. It enables compliance and informed decisions.

4. Assign Risks to Team Members

Actors: Project Manager, SystemLinked FR: FR-001, FR-006User Stories: Assign Risks, Manage Roles

Explanation:This workflow ensures risk items are delegated to the right personnel. Assignment depends on availability and expertise, helping with accountability and role-based workflows.

5. Generate Real-Time Alerts

Actors: SystemLinked FR: FR-005 (Real-Time Alerts)User Stories: Generate Alerts, Link Incidents

Explanation:System monitors for new risks or thresholds and triggers alerts. The alerts are logged and shared with stakeholders instantly to reduce delay in response.

6. Manage User Roles and Permissions

Actors: AdminLinked FR: FR-006 (Manage Roles)User Stories: Manage Roles, Support Concurrent Users

Explanation:Admins can view, assign, or revoke roles from users. This workflow supports access control and ensures appropriate permissions across the system.

7. Link Risks to Past Incidents

Actors: Analyst, SystemLinked FR: FR-007 (Link Incidents)User Stories: Link Risks

Explanation:Analysts can link current risks to past incidents for context and better understanding. System validates linkage and ensures no duplication.

8. Automated Data Backup Process

Actors: SystemLinked FR: FR-011 (Automated Data Backups)User Stories: Backup System

Explanation:This fully automated process ensures regular backups, verifies integrity, and retries on failure. Supports disaster recovery needs.
