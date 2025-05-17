# 📊 Risk Management System

## 🧾 Project Overview

The **Risk Management System (RMS)** is a full-stack solution designed to allow organizations to identify, assess, mitigate, and monitor risks in real time. Built using Agile methodologies, the system has evolved through structured assignments that focused on key aspects of software development: from requirements gathering to clean architecture, testing, DevOps integration, and CI/CD automation.
Links to:
- [SPECIFICATION.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/SPECIFICATION.md) (System Specification)
- [ARCHITECTURE.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/ARCHITECTURE.md) (C4 Diagrams and Architecture)
- [STAKEHOLDER_ANALYSIS.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/STAKEHOLDER_ANALYSIS.md) (Stakeholder table)
- [SYSTEM_REQUIREMENTS.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/SYSTEM_REQUIREMENTS.md) (System requirements)
- [USE CASE DIAGRAM.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B5%5D/Use_case_diagram.md)(Use case diagram)
- [USE CASE SPECIFICATION.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B5%5D/Use%20_case_specification.md) (Use case specification)
- [TEST CASES.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B5%5D/Test_cases.md) (Test cases)
- [USE CASE REFLECTIONS.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B5%5D/Reflection.md)(Reflections)
- [REFLECTION.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/REFLECTION.md) (Reflection and challenges)
- [USE STORIES.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B6%5D/User_Stories.md) (User stories)
- [SPRINT PLANNING.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B6%5D/Sprint%20Planning.md) (Sprints)
- [PRODUCT BACKLOG.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B6%5D/Product%20Backlog.md) (Backlog)
- [STATE TRANSACTION DIAGRAM.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B8%5D/State_Transaction_Diagram.md)(Transaction diagram)
- [ACTIVITY DIAGRAM.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B8%5D/Activity_Diagram). (Activity diagram)
- [EXPLANATION FOR TRANSACTION DIAGRAM.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B8%5D/Transaction_Diagram_Explanation.md) (Explanation)
- [EXPLANATION FOR  ACTIVITY DIAGRAM.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B8%5D/Activity_Diagram_Explanation.md) (Explanation)
- [DIAGRAM REFLECTIONS.md](https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System/blob/main/Ass%5B8%5D/Reflections.md) (Diagram reflection)

## Domain: 
The system falls under the domain of **Business Operations,Organisations and Risk Management**, which helps businesses identify, analyze, and respond to potential risks in an organized manner.

## Problem Statement: 
The purpose of this system is to streamline the process of identifying risks within an organization and developing mitigation plans for these risks. The system will help companies respond quickly to risks, reduce uncertainties, and minimize financial losses.

---

## Things you will find in this Project

* [Project Overview](#-project-overview)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Directory Structure](#-directory-structure)
* [Setup Instructions](#-setup-instructions)
* [Development Process](#-development-process)
* [API Documentation](#-api-documentation)
* [Creational Patterns Used](#-creational-patterns-used)
* [Test Coverage](#-test-coverage)
* [CI/CD](#-cicd)
* [Security & Licensing](#-security--licensing)
* [Roadmap](#-roadmap)
* [Contributing](#-contributing)

---

## ✅ Features

* Create, update, delete risks with severity and likelihood levels
* Assign risks to team members
* Build and approve mitigation plans
* User authentication and role-based access
* Generate compliance and audit reports
* Real-time risk alerts
* RESTful API built with FastAPI
* Integration-tested with CI/CD pipelines
* Modular design using SOLID principles

---

## 💻 Tech Stack

| Layer           | Technology                                               |
| --------------- | -------------------------------------------------------- |
| Backend         | Python, FastAPI                                          |
| Design Patterns | Factory, Singleton, Builder, Prototype, Abstract Factory |
| Testing         | Pytest                                                   |
| Persistence     | In-memory storage, designed for extension to JSON/SQL    |
| CI/CD           | GitHub Actions                                           |

---

## 🗂️ Directory Structure

```
.
├── Ass[10]/Assignment10         # Class design and creational patterns
├── Ass[11]/Assignment11         # Repository abstraction and implementation
├── Ass[12]/Assignment12         # RESTful API, service layer, OpenAPI, tests
├── Ass[13]/Assignment13         # GitHub Actions CI/CD workflows
├── Ass[14]/Assignment14         # Project cleanup, licensing, contribution guide
```

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repo
$ git clone https://github.com/Ongeziwe-Qwayede-01/Risk-Management-System.git
$ cd Risk-Management-System

# 2. Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Run the API
$ uvicorn main:app --reload
```

---

## 🧱 Development Process

### Assignment Breakdown:

* **Assignment 3-4**: Stakeholder analysis, functional & non-functional requirements
* **Assignment 5-6**: Use case modeling, test cases, Agile sprint planning
* **Assignment 7-8**: Kanban board setup, state and activity diagrams
* **Assignment 9**: Domain modeling and class diagram design
* **Assignment 10**: Class implementation and creational pattern usage
* **Assignment 11**: Repository abstraction, dependency injection
* **Assignment 12**: API endpoints and integration with services
* **Assignment 13**: GitHub Actions CI pipeline
* **Assignment 14**: Project cleanup, LICENSE, CONTRIBUTING, ROADMAP

---

## 📚 API Documentation

Once the server is running, access the OpenAPI docs:

```
http://127.0.0.1:8000/docs
```

Includes endpoints for:

* `/risks` – risk management
* `/users` – user accounts
* `/mitigation-plans` – mitigation tracking

---

## 🏗️ Creational Patterns Used

* **Simple Factory**: Creating user roles (Admin, Analyst)
* **Factory Method**: Notification processor (email, SMS)
* **Abstract Factory**: Generating various types of reports
* **Builder**: Constructing mitigation plans step-by-step
* **Prototype**: Cloning alert configurations
* **Singleton**: Shared DB connection

---

## ✅ Test Coverage

* **tests/api/**: Endpoint integration tests
* **tests/services/**: Unit tests for business logic
* Run using `pytest`:

```bash
pytest --cov=.
```

---

## 🚀 CI/CD

* Built with **GitHub Actions**
* Lints, tests and builds on each PR
* `.github/workflows/ci.yml` includes test + build jobs

---

## 🔒 Security & Licensing

* Data validation using Pydantic
* AES-256 encryption logic planned
* RBAC implemented via service layer
* Licensed under MIT License – see [LICENSE](LICENSE)

---

## 🗺️ Roadmap – Risk Management System

### ✅ Completed

* Risk CRUD operations
* Mitigation Plan workflow
* User management
* REST API with FastAPI
* Test coverage and CI via GitHub Actions

### 🚧 Upcoming Features

* [ ] Export risk reports to PDF
* [ ] Add Redis for alert caching
* [ ] Email notifications for high-severity risks
* [ ] Admin dashboard UI with React
* [ ] OAuth2 Authentication

---

## 🙌 Contributing

* See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details
* Open issues labeled `good-first-issue` are beginner friendly
* All contributions must be via PR – no direct `main` pushes

---

**Author:** Ongeziwe Qwayede
**CPUT BCom IS Graduate | Software Developer**


