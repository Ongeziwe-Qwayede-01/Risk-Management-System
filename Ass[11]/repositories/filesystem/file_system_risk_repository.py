import json
from src.risk import Risk
from repositories.risk_repository import RiskRepository

class FileSystemRiskRepository(RiskRepository):
    def __init__(self, file_path):
        self._file_path = file_path

    def save(self, risk: Risk):
        raise NotImplementedError("Coming soon...")

    def find_by_id(self, risk_id: str):
        raise NotImplementedError("Coming soon...")

    def find_all(self):
        raise NotImplementedError("Coming soon...")

    def delete(self, risk_id: str):
        raise NotImplementedError("Coming soon...")
