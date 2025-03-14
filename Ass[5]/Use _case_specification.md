# **Risk Management System - Use Case Specifications**

## **1. Use Case: Identify Risk**
**Actor :** Risk Manager  
**Description:**  
The Risk Manager logs a new risk in the system, categorizing and assessing its likelihood and impact.  

**Precondition:**  
- The Risk Manager is logged into the system.  
- The organization has at least one active project or department to assign the risk.  

**Postcondition:**  
- A new risk entry is created with a unique ID.  
- A notification is sent to the Compliance Officer for review.  

### **Basic Flow:**
1. Risk Manager selects "Identify Risk" from the system dashboard.
2. System prompts for risk details (category, severity, likelihood).
3. Risk Manager enters details and submits.
4. System validates input and stores the risk.
5. System notifies the Compliance Officer.

### **Alternative Flows:**
- **Risk Manager enters incomplete data** → System prompts for missing fields.
- **Database error while saving risk** → System logs the error and alerts the admin.

---

## **2. Use Case: Assess Risk Impact**
**Actor :** Risk Manager  
**Description:**  
The Risk Manager evaluates the impact of an identified risk, including financial loss, regulatory issues, and reputational damage.  

**Precondition:**  
- A risk entry must exist in the system.  
- The Risk Manager is assigned to assess risks.  

**Postcondition:**  
- The risk impact assessment is updated and saved.  
- A detailed risk report is generated.  

### **Basic Flow:**
1. Risk Manager selects a risk from the system.
2. System displays current risk details.
3. Risk Manager enters impact assessment details.
4. System updates the risk impact report.

### **Alternative Flows:**
- **Risk does not exist** → System notifies the user.
- **Invalid data format** → System prompts for corrections.

---

## **3. Use Case: Mitigate Risk**
**Actor :** Risk Manager  
**Description:**  
The Risk Manager submits a mitigation plan to reduce or eliminate the risk.  

**Precondition:**  
- The risk must be active and not already mitigated.  

**Postcondition:**  
- A mitigation plan is created and sent for approval.  

### **Basic Flow:**
1. Risk Manager selects an active risk.
2. System prompts for mitigation strategies.
3. Risk Manager submits the mitigation plan.
4. System stores the plan and notifies the Compliance Officer.

### **Alternative Flows:**
- **Mitigation plan is missing key details** → System prompts the user.
- **Risk is already mitigated** → System prevents duplicate submission.

---

## **4. Use Case: Approve Mitigation Plan**
**Actor :** Compliance Officer  
**Description:**  
The Compliance Officer reviews and approves mitigation plans before implementation.  

**Precondition:**  
- A mitigation plan must be submitted.  
- The Compliance Officer has permissions to approve risks.  

**Postcondition:**  
- The mitigation plan is approved or rejected.  

### **Basic Flow:**
1. Compliance Officer selects a mitigation plan for review.
2. System displays plan details.
3. Compliance Officer approves or rejects the plan.
4. If approved, the system updates the risk status.

### **Alternative Flows:**
- **Plan lacks required details** → Compliance Officer requests revisions.
- **Plan is rejected** → System marks the risk as "Rejected" and notifies the Risk Manager.

---

## **5. Use Case: Monitor Risk**
**Actor :** Risk Manager, System (Automated Process)  
**Description:**  
Tracks and updates risk levels, sending alerts for significant changes.  

**Precondition:**  
- At least one active risk exists in the system.  

**Postcondition:**  
- Risk status is updated.  
- Stakeholders are notified if risk levels change.  

### **Basic Flow:**
1. System automatically checks risk statuses.
2. If conditions change, system updates risk severity.
3. System notifies Risk Manager.
4. Risk Manager reviews updated data.

### **Alternative Flows:**
- **No changes in risk level** → No alerts are sent.
- **System fails to fetch data** → Admin is notified.

---

## **6. Use Case: Generate Risk Report**
**Actor :** Executive  
**Description:**  
Generates a summary report of organizational risks and their statuses.  

**Precondition:**  
- The system has recorded risk data.  
- The user has reporting access.  

**Postcondition:**  
- A risk report is generated.  

### **Basic Flow:**
1. Executive selects "Generate Report."
2. System compiles risk data.
3. System formats the report.
4. Executive downloads or views the report.

### **Alternative Flows:**
- **No risk data available** → System notifies the user.
- **Report generation error** → Admin is notified.

---

## **7. Use Case: Configure Risk Thresholds**
**Actor :** Admin  
**Description:**  
Allows Admins to define risk severity levels and notification settings.  

**Precondition:**  
- Admin is logged in with permissions.  

**Postcondition:**  
- System updates risk thresholds.  

### **Basic Flow:**
1. Admin navigates to settings.
2. Admin modifies threshold values.
3. System saves the changes.

### **Alternative Flows:**
- **Invalid threshold values** → System prompts for corrections.
- **System error during update** → Changes are rolled back.

---

## **8. Use Case: Manage User Access**
**Actor :** Admin  
**Description:**  
Assigns roles and permissions for users.  

**Precondition:**  
- Admin is logged in.  

**Postcondition:**  
- User permissions are updated.  

### **Basic Flow:**
1. Admin selects "User Management."
2. System displays users.
3. Admin updates roles and permissions.
4. System saves changes.

### **Alternative Flows:**
- **User does not exist** → System displays an error.
- **Insufficient privileges** → System restricts access.

---

# **Final Notes**
This document provides structured use case specifications for the **Risk Management System**, ensuring **clarity and completeness** in tracking, assessing, mitigating, and reporting risks.

