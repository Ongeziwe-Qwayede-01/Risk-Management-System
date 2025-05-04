# 📘 Risk Management System – Assignment 12

This is a FastAPI-based Risk Management System demonstrating layered architecture, repository design patterns, and full CRUD support for risks, users, and mitigation plans.

---

## Project Structure
```
Ass[12]/
├── api/                      # FastAPI route handlers
├── services/                 # Business logic
├── repositories/            # Interfaces + in-memory data storage
├── src/                     # Domain models
├── tests/                   # Unit and integration tests
├── docs/                    # API documentation (optional)
├── main.py                  # FastAPI app entry point
└── README.md                # Project guide
```

---

## Technologies Used
- Python 3.10+
- FastAPI
- Pydantic (implicit via FastAPI)
- Uvicorn
- Pytest

---

## Features
- Manage Risks with severity and likelihood
- Track Users and assign roles
- Handle Mitigation Plans and approve workflows
- Testable and maintainable with clear separation of concerns

---

## Running the Project
1. **Install dependencies**:
```bash
pip install fastapi uvicorn pytest
```

2. **Start the API server**:
```bash
uvicorn main:app --reload
```

3. **Access Documentation**:
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc
![Screenshot 2025-05-04 184853](https://github.com/user-attachments/assets/75bc2d37-e0c0-4109-b484-b781b962e9be)

---

## Running Tests
```bash
pytest tests/
```

---

## Folder-by-Folder Overview
- `api/`: Exposes endpoint routes for risks, users, and mitigation plans.
- `services/`: Contains reusable business logic for all core modules.
- `repositories/`: Provides in-memory storage but can be extended to real DBs.
- `src/`: Defines `Risk`, `User`, and `MitigationPlan` models.
- `tests/`: Organized test files per service and route layer.

---
## GitHub Project Board showing completed tasks
![Screenshot 2025-05-04 185114](https://github.com/user-attachments/assets/155a0bd9-597d-4d4a-a8b8-24d0f6b0ec88)

---

## Notes
- The repository structure supports **easy swapping** between in-memory, filesystem, or real DB storage.
- Implements **Separation of Concerns** for high maintainability.

---


