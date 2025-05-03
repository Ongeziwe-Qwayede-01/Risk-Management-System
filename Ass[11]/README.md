# Assignment 11 – Repository Pattern Integration  
**Project:** Risk Management System (RMS)

---

## Objective

This assignment implements the **Repository Pattern** in the Risk Management System to separate business logic from data access logic. The goal is to make the system modular, scalable, and easily testable. The primary focus is to start with an **in-memory repository** and **design for easy replacement** with other data stores like JSON, databases, or APIs in the future.

---

## Features Implemented

### Repository Interface

- A base `Repository` class defines common operations like `save`, `find_by_id`, `delete`, and `list_all`.
- `RiskRepository` extends the base class with a concrete interface specific to `Risk` entities.

---

### In-Memory Implementation

- `InMemoryRiskRepository` uses a Python dictionary (like a HashMap) to store risk data.
- Ideal for development and unit testing.
- Fast and doesn’t require external dependencies.

---

### Factory Class

- `RepositoryFactory` returns an appropriate implementation (`in-memory` for now).
- Future storage types like files, SQL, or API can be returned based on a config or parameter.
- Enables **swappable repositories** with a single change in the factory method.

---

### Unit Testing

- Tests for the in-memory repository validate saving, retrieving, deleting, and listing risks.
- Written using Python’s `unittest` framework.
- Located in the `/tests` folder.
- Provides high test coverage without involving real storage systems.


---

## Design Strategy

The RMS is designed with future extensibility in mind. Right now, it uses an **in-memory HashMap**, but the system is architected to support:

| Storage Option           | Status       | Purpose                            |
|--------------------------|--------------|-------------------------------------|
| In-Memory              | Implemented | For testing & prototyping           |
| JSON / XML Files       | Stubbed     | For local file storage              |
| SQL / NoSQL DBs        | Designed    | For future scalability              |
|  External REST APIs     | Designed    | For cloud or microservice setups    |

The repository layer is fully decoupled from the business logic. Switching implementations only requires an update in the `RepositoryFactory`.

---

## How to Run

```bash
cd Ass[11]
python main.py

