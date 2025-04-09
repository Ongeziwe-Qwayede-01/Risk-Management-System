# RMS Domain Modeling and Class Diagram



---

## Domain Model 

| **Class**     | **Attributes**                               | **Methods**                          | **Relationships**                           |
|---------------|----------------------------------------------|--------------------------------------|---------------------------------------------|
| Risk          | id, description, type, status                | create(), update(), evaluate()       | Associated with MitigationPlan              |
| MitigationPlan| id, strategy, status                         | submit(), approve(), revise()        | Linked to Risk, Tasks                        |
| User          | userId, name, role                           | login(), logout(), manageRole()      | Inherits from Person                         |
| Analyst       | expertise                                    | reviewRisk(), linkIncidents()        | Inherits from User                           |
| Admin         | accessLevel                                  | manageUsers(), assignRoles()         | Inherits from User                           |
| Alert         | id, message, timestamp                       | trigger(), notifyStakeholders()      | Associated with Risk                         |
| Task          | id, description, assignedTo, dueDate         | assign(), markComplete()             | Part of MitigationPlan                       |
| Incident      | id, reportDate, summary                      | linkRisk(), analyzeImpact()          | Linked to Risk                               |
| Backup        | id, timestamp, status                        | startBackup(), verifyIntegrity()     | System-triggered                             |

