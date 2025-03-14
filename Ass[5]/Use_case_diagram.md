![Use Case Diagram](https://www.mermaidchart.com/raw/adac722e-cd7f-4b9a-8097-2f3d9962476f?theme=light&version=v0.1&format=svg)
# **Use Case Explanation for Risk Management System**

## **Key Actors and Their Roles**
The Risk Management System involves several key actors who interact with the system to identify, assess, mitigate, and monitor risks. Below is a breakdown of each actor and their responsibilities:

| **Actor**             | **Role & Responsibilities** |
|----------------------|---------------------------|
| **Admin**           | - Manages user accounts, roles, and access permissions.<br> - Configures system settings related to risk management workflows.<br> - Ensures data integrity and system security. |
| **Risk Manager**    | - Identifies potential risks in the organization.<br> - Logs risk details including category, severity, and impact level.<br> - Initiates risk mitigation plans and submits them for approval. |
| **Compliance Officer** | - Monitors the organization’s adherence to risk policies and regulations.<br> - Reviews risk logs and verifies mitigation actions.<br> - Ensures the system meets legal and regulatory requirements. |
| **Executive**       | - Reviews high-level risk reports to support decision-making.<br> - Analyzes trends in risk data to improve business strategy.<br> - Ensures appropriate resources are allocated to risk mitigation. |
| **System (Automated Process)** | - Generates real-time alerts for critical risk incidents.<br> - Stores and retrieves historical risk data for analysis.<br> - Provides an audit trail for tracking changes in risk management. |

---

## **Relationships Between Actors and Use Cases**
In the **Risk Management System**, different actors interact with use cases, often following specific relationships such as **inclusion** and **extension** to ensure a seamless risk management workflow.

### **1. Inclusion Relationship**
**Example: "Mitigate Risk" includes "Approve Mitigation Plan".**
- Before a mitigation action can be implemented, a **Risk Manager** must submit a mitigation plan.
- The **Compliance Officer** is responsible for reviewing and approving the plan before any risk mitigation actions can be executed.
- This inclusion ensures risk mitigation follows a **governance and approval** process.

### **2. Extension Relationship**
**Example: "Assess Risk Impact" extends "Identify Risk".**
- A **Risk Manager** first **identifies a risk** by entering risk details into the system.
- If additional analysis is needed, the system extends this process by triggering an **impact assessment**, where the severity and likelihood of the risk are evaluated.
- This **extension** allows for **conditional actions** only when necessary.

---

## **How the Diagram Addresses Stakeholder Concerns**
The Use Case Diagram ensures that key stakeholder concerns from **Assignment 4** are addressed through system functionality:

1. **Security vs Usability**
   - The **Admin** controls user access to sensitive risk data.
   - The **Compliance Officer** ensures that security policies are enforced while keeping reports accessible to executives.

2. **Real-Time Data vs Performance**
   - The **System** generates real-time alerts to notify stakeholders about new risks without overloading the database.
   - **Executives** receive processed, summarized reports instead of raw data, optimizing performance.

3. **Scalability**
   - The system supports both **small businesses and large enterprises** by allowing **configurable risk categories and assessment criteria**.
   - Audit logs and risk reports are structured for both **operational teams and executive decision-makers**.

---

This structured approach ensures that the **Risk Management System** aligns with stakeholder expectations and business requirements, providing a **robust framework** for managing organizational risks effectively.

