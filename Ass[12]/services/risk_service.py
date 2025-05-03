# services/risk_service.py

from repositories.risk_repository import RiskRepository
from src.risk import Risk
from uuid import uuid4

class RiskService:
    def __init__(self, repository: RiskRepository):
        self.repository = repository

    def create_risk(self, description, severity, likelihood):
        if not description or not severity or not likelihood:
            raise ValueError("All risk fields must be provided")

        risk = Risk(
            id=str(uuid4()),
            description=description,
            severity=severity,
            likelihood=likelihood
        )
        self.repository.save(risk)
        return risk

    def get_all_risks(self):
        return self.repository.list_all()

    def get_risk_by_id(self, risk_id):
        return self.repository.find_by_id(risk_id)

    def update_risk(self, risk_id, description, severity, likelihood):
        existing = self.repository.find_by_id(risk_id)
        if not existing:
            raise ValueError("Risk not found")

        existing.description = description
        existing.severity = severity
        existing.likelihood = likelihood
        self.repository.save(existing)
        return existing

    def delete_risk(self, risk_id):
        self.repository.delete(risk_id)
        return True
