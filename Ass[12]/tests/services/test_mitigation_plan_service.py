from services.mitigation_plan_service import MitigationPlanService
from repositories.inmemory.in_memory_mitigation_plan_repository import InMemoryMitigationPlanRepository

def test_create_and_approve_plan():
    repo = InMemoryMitigationPlanRepository()
    service = MitigationPlanService(repo)
    plan = service.create_plan("risk123", ["Add firewall", "Train staff"])
    assert plan.approved is False
    approved_plan = service.approve_plan(plan.id)
    assert approved_plan.approved is True
