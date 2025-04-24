from typing import Optional
from repositories.risk_repository import RiskRepository
from src.risk import Risk  # adjust this import path as needed

class InMemoryRiskRepository(RiskRepository):
    def __init__(self):
        self._storage = {}

    def save(self, risk: Risk) -> None:
        self._storage[risk.risk_id] = risk

    def find_by_id(self, risk_id: str) -> Optional[Risk]:
        return self._storage.get(risk_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, risk_id: str) -> None:
        if risk_id in self._storage:
            del self._storage[risk_id]
