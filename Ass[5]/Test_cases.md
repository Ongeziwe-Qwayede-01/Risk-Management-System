# **Test Case Development - Risk Management System**

## **Functional Test Cases**

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|-----------------|-----------------|----------------|-----------|------------------|----------------|------------------|
| TC-001 | FR-001 | Identify a new risk | 1. Login as Risk Manager  2. Navigate to "Identify Risk" 3. Enter risk details 4. Click "Submit" | System saves the risk and generates a unique ID | | |
| TC-002 | FR-002 | Assess risk impact | 1. Login as Risk Manager 2. Select an existing risk 3. Enter impact details 4. Click "Save" | System updates risk impact assessment | | |
| TC-003 | FR-003 | Submit mitigation plan | 1. Login as Risk Manager 2. Select an active risk 3. Enter mitigation details 4. Click "Submit" | System saves mitigation plan and notifies Compliance Officer | | |
| TC-004 | FR-004 | Approve mitigation plan | 1. Login as Compliance Officer 2. Select mitigation plan 3. Click "Approve" | System updates risk status to "Mitigated" | | |
| TC-005 | FR-005 | Generate risk report | 1. Login as Executive 2. Navigate to "Reports" 3. Click "Generate Report" | System generates a report with risk summaries | | |
| TC-006 | FR-006 | Monitor risks | 1. System runs automated risk monitoring 2. Check risk severity levels | System updates risk severity and notifies Risk Manager | | |
| TC-007 | FR-007 | Configure risk thresholds | 1. Login as Admin 2. Navigate to "Settings" 3. Modify threshold values 4. Click "Save" | System saves new threshold values | | |
| TC-008 | FR-008 | Manage user access | 1. Login as Admin 2. Navigate to "User Management" 3. Change user roles 4. Click "Save" | System updates user roles and permissions | | |

---

## **Non-Functional Test Cases**

| **Test Case ID** | **Requirement ID** | **Description** | **Test Scenario** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|-----------------|-----------------|----------------|----------------|------------------|----------------|------------------|
| TC-009 | NFR-001 | Performance Testing | Simulate 1,000 concurrent users submitting risks | System should handle requests without crashing, and response time should be ≤ 2 seconds | | |
| TC-010 | NFR-002 | Security Testing | Attempt unauthorized access to modify risk data | System should prevent unauthorized access and log the attempt | | |

---

## **Final Notes**
- **Functional tests** verify that risk management features work correctly.
- **Performance and security tests** ensure the system can handle high loads and remains secure.  



