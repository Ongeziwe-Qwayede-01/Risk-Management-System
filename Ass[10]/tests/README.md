##  How to Run Tests

Esure the virtual environment is activated, then run:

```bash
pytest tests/
```

To generate a **coverage report**, install:

```bash
pip install pytest-cov
pytest --cov=creational_patterns tests/
```