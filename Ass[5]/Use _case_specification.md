# **Risk Management System - Use Case Specifications**

## **1. Identify Risk**
**Actor:** Risk Manager  
**Description:** This use case allows a Risk Manager to log a new risk in the system, defining its category, impact level, and likelihood.  
**Precondition:** The Risk Manager is logged in and has the necessary permissions.  
**Postcondition:** A new risk entry is created in the system.  

### **Basic Flow:**
1. Risk Manager selects "Identify Risk" from the system dashboard.
2. System prompts for risk details (category, severity, likelihood).
3. Risk Manager enters details and submits.
4. System stores the risk and assigns it a unique ID.
5. System notifies the Compliance Officer.

### **Alternative Flows:**
- **Risk Manager enters incomplete data** → System prompts for missing information.
- **System encounters a database error** → System displays an error message and logs the failure.

---

## **2. Assess Risk Impact**
**Actor:** Risk Manager  
**Description:** This use case evaluates the potential consequences of an identified risk.  
**Precondition:** A risk must already exist in the system.  
**Postcondition:** Risk assessment report is updated.  

### **Basic Flow:**
1. Risk Manager selects a risk from the list.
2. System prompts for impact analysis inputs (e.g., financial loss, compliance issues).
3. Risk Manager completes the form and submits.
4. System updates the risk impact assessment and generates a report.

### **Alternative Flows:**
- **Risk does not exist** → System notifies the user and redirects to the risk identification page.
- **Invalid input format** → System prompts the Risk Manager to correct the entry.

---

## **3. Mitigate Risk**
**Actor:** Risk Manager  
**Description:** Proposes and submits mitigation actions for an identified risk.  
**Precondition:** Risk must have an active status and not be mitigated.  
**Postcondition:** Mitigation plan is created and awaits approval.  

### **Basic Flow:**
1. Risk Manager selects an open risk.
2. System displays available mitigation strategies.
3. Risk Manager selects an appropriate strategy and submits a mitigation plan.
4. System stores the mitigation plan and notifies the Compliance Officer.

### **Alternative Flows:**
- **Mitigation plan is missing required details** → System prompts the user.
- **Risk is already mitigated** → System prevents duplicate submission.

---

## **4. Approve Mitigation Plan**
**Actor:** Compliance Officer  
**Description:** Ensures that proposed mitigation plans meet compliance standards before implementation.  
**Precondition:** A mitigation plan must be submitted.  
**Postcondition:** Mitigation plan is approved or rejected.  

### **Basic Flow:**
1. Compliance Officer selects a mitigation plan for review.
2. System displays details of the plan.
3. Compliance Officer either approves or rejects the plan.
4. If approved, the system marks the risk as "Mitigation in Progress."
5. System notifies the Risk Manager.

### **Alternative Flows:**
- **Plan is missing key details** → Compliance Officer requests revisions.
- **Compliance Officer rejects the plan** → System marks the plan as "Rejected" and notifies the Risk Manager.

---

## **5. Monitor Risk**
**Actor:** Risk Manager, System (Automated Process)  
**Description:** Tracks risk status, updates risk levels, and notifies stakeholders of significant changes.  
**Precondition:** At least one active risk exists in the system.  
**Postcondition:** Risk log is updated, and relevant stakeholders are notified.  

### **Basic Flow:**
1. System runs scheduled checks on risk status.
2. If conditions change, system updates risk severity and sends alerts.
3. Risk Manager reviews updated risk data.
4. If necessary, additional mitigation actions are planned.

### **Alternative Flows:**
- **No changes in risk level** → No alerts are sent.
- **System fails to fetch data** → Admin is notified to check the system logs.

---

## **6. Generate Risk Report**
**Actor:** Executive  
**Description:** Provides a summary of organizational risks, including trends, mitigated risks, and ongoing assessments.  
**Precondition:** System has recorded risk data.  
**Postcondition:** Risk report is generated and available for review.  

### **Basic Flow:**
1. Executive selects "Generate Report."
2. System retrieves and compiles risk data.
3. System formats the report (PDF, Excel, or web view).
4. Executive downloads or views the report.

### **Alternative Flows:**
- **No risks logged** → System notifies that no data is available for reporting.
- **System error while generating report** → User is notified, and logs are recorded for admin review.

---

## **7. Configure Risk Thresholds**
**Actor:** Admin  
**Description:** Defines the risk severity levels and notification settings.  
**Precondition:** Admin is logged in with sufficient privileges.  
**Postcondition:** System updates risk thresholds.  

### **Basic Flow:**
1. Admin navigates to system settings.
2. Admin modifies threshold values (e.g., high-risk threshold at 80% probability).
3. System saves the new settings.
4. System applies the changes to all risk assessments.

### **Alternative Flows:**
- **Invalid threshold values** → System rejects input and provides guidelines.
- **System error during update** → Changes are rolled back, and the admin is notified.

---

## **8. User Access Management**
**Actor:** Admin  
**Description:** Manages user roles and permissions to ensure security compliance.  
**Precondition:** Admin is logged in.  
**Postcondition:** User permissions are updated.  

### **Basic Flow:**
1. Admin selects "User Management."
2. System displays a list of users.
3. Admin selects a user and modifies role/permissions.
4. System saves changes and updates access controls.

### **Alternative Flows:**
- **User does not exist** → System displays an error.
- **Insufficient admin privileges** → System restricts access to modifications.

---

# **Final Notes**
This document provides a structured overview of the **8 critical use cases** for the Risk Management System. Each use case includes:
- **Detailed descriptions**
- **Preconditions and postconditions**
- **Main and alternative flows**






