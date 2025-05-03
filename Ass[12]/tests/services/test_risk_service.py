from services.risk_service import RiskService
from repositories.inmemory.in_memory_risk_repository import InMemoryRiskRepository

def test_create_and_get_risk():
    repo = InMemoryRiskRepository()
    service = RiskService(repo)
    risk = service.create_risk("Cyberattack", "High", "Likely")
    retrieved = service.get_risk_by_id(risk.id)
    assert retrieved.description == "Cyberattack"