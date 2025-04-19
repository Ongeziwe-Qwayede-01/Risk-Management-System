# Object State Model Explanations – Risk Management System (RMS)

This document outlines the key object state transitions for 8 critical objects in the RMS application. Each section maps the object’s lifecycle to functional requirements and user stories defined in earlier assignments.

---

## 1. Risk Object

**Description**:  
Represents the full lifecycle of a risk within the system, from identification to closure. Risks are assessed, approved, mitigated, monitored, and eventually archived for historical analysis.

- **Key States**: `Identified` → `Assessed` → `Approved` → `Monitored` → `Mitigated` → `Closed` → `Archived`
- **Transitions**: Triggered by actions like user assignments, approvals, or mitigation completion.

**Linked Functional Requirement**: FR-001 (Identify and Assess Risks)  
**Related User Stories**:  
- Identify Risks  
- Assign Risks  
- Monitor Risks  

---

## 2. Mitigation Plan

**Description**:  
Tracks how a mitigation plan evolves from being drafted to implemented. It includes review and testing phases, ensuring that the response to a risk is controlled and effective.

- **Key States**: `Drafted` → `Submitted` → `Reviewed` → `Approved` → `Implemented` → `Closed` → `Archived`
- **Transitions**: Initiated by submission, review approval, or test completion.

**Linked Functional Requirement**: FR-002 (Approve Mitigation Plans)  
**Related User Stories**:  
- Approve Mitigation Plans  
- Assign Tasks  

---

## 3. User Account

**Description**:  
Represents a user’s account lifecycle, including the different states an account may enter due to user actions or system policies (e.g., security restrictions).

- **Key States**: `Registered` → `Active` → `Suspended` → `Deactivated`
- **Transitions**: Triggered by login, admin actions, or policy enforcement.

**Linked Functional Requirement**: FR-006 (Manage User Roles and Permissions)  
**Related User Stories**:  
- Manage Roles  
- Support Concurrent Users  

---

## 4. Risk Report

**Description**:  
Shows the lifecycle of a risk report used by stakeholders. After generation, a report can be reviewed, approved, or sent for revisions. Final versions are distributed or stored.

- **Key States**: `Generated` → `In Review` → `Approved` → `Published`
- **Transitions**: Triggered by report submission, reviews, or approval decisions.

**Linked Functional Requirement**: FR-003 (Review Risk Reports)  
**Related User Stories**:  
- Review Reports  
- Generate Compliance Reports  

---

## 5. Compliance Report

**Description**:  
Represents a specialized report submitted to regulators. It can be accepted or rejected and may require resubmission. Used to meet external audit and compliance requirements.

- **Key States**: `Generated` → `Submitted` → `Under Review` → `Accepted` / `Rejected`
- **Transitions**: Based on external feedback or internal resubmission.

**Linked Functional Requirement**: FR-008 (Generate Compliance Reports)  
**Related User Stories**:  
- Generate Compliance Reports  

---

## 6. Alert

**Description**:  
Handles real-time alerts triggered by system anomalies or risk thresholds. Alerts can be acknowledged, escalated, or resolved by users.

- **Key States**: `Generated` → `Acknowledged` → `In Progress` → `Resolved` → `Closed`
- **Transitions**: Based on user responses or system resolution mechanisms.

**Linked Functional Requirement**: FR-005 (Generate Real-Time Alerts)  
**Related User Stories**:  
- Generate Alerts  
- Link Risks to Incidents  

---

## 7. Audit Log

**Description**:  
Logs system/user actions. Each entry is immutable but can be accessed or filtered for auditing purposes. Crucial for traceability and legal compliance.

- **Key States**: `Created` → `Stored` → `Accessed` (Read-only)
- **Transitions**: System-generated and accessed on demand.

**Linked Functional Requirement**: FR-010 (Log Risk Actions for Audit)  
**Related User Stories**:  
- Log Actions  
- Manage History  

---

## 8. Backup Job

**Description**:  
Represents a recurring system process for backing up data. It can succeed, fail, or be retried. Critical for disaster recovery and system reliability.

- **Key States**: `Scheduled` → `Running` → `Success` / `Failed` → `Retried` (if failed) → `Completed`
- **Transitions**: Based on time-based triggers and job outcomes.

**Linked Functional Requirement**: FR-011 (Automated Data Backups)  
**Related User Stories**:  
- Backup System  
- Handle Failures  



