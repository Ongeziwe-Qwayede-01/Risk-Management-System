# 🛠️ Creational Patterns – Risk Management System

This folder contains the implementation of all six major creational design patterns used in the Risk Management System (RMS) to control object creation and promote flexibility, scalability, and testability.

---

## 1. Simple Factory

**Used For**: Creating different types of system users (e.g., Analyst, Admin) from a central factory.

**Why**: Centralizes the logic of user creation and enforces role-based instantiation.

---

## 2. Factory Method

**Used For**: Creating different types of `NotificationProcessor` objects (e.g., EmailNotification, SMSNotification) that follow a common interface.

**Why**: The Risk Management System must send alerts through multiple channels (email, SMS, or app). Each channel requires different logic, but they all follow the same interface (`send_alert(message)`).

- It supports FR-005: “Generate Real-Time Alerts”
- It reflects user stories like “Generate Alerts” and “Notify Responsible Users”
- It allows easily adding more notification channels in the future without modifying existing code.


---

## 3. Abstract Factory

**Used For**: Creating families of related reports like `ComplianceReport` and `RiskReport` through `ReportFactory`.

**Why**: Ensures that objects in a family (e.g., different types of reports) are created together with consistent interfaces and formatting.

---

## 4. Builder

**Used For**: Constructing complex `MitigationPlan` objects step-by-step using a fluent builder.

**Why**: Some plans may have optional fields, deadlines, or review stages. Builder separates the construction process from representation.

---

## 5. Prototype

**Used For**: Cloning frequently used or preconfigured `Alert` objects from a cache to avoid expensive recreation.

**Why**: Improves performance and ensures consistent templates for repeated high-priority alerts.

---

## 6. Singleton

**Used For**: Ensuring a single `DatabaseConnection` instance is shared across the system.

**Why**: Prevents multiple connections being opened to the database at once, which reduces resource usage and prevents connection leaks.

---

Each pattern is used where it provides clear design benefits in the RMS, and all implementations are located in separate subfolders for modularity and clarity.
