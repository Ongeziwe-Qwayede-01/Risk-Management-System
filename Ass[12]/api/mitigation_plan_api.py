from fastapi import APIRouter, HTTPException
from services.mitigation_plan_service import MitigationPlanService
from repositories.inmemory.in_memory_mitigation_plan_repository import InMemoryMitigationPlanRepository
from repositories.inmemory.in_memory_risk_repository import InMemoryRiskRepository

router = APIRouter()

mitigation_service = MitigationPlanService(
    InMemoryMitigationPlanRepository(),
    InMemoryRiskRepository()
)

@router.post("/plans")
def create_plan(risk_id: str, steps: str):
    try:
        return mitigation_service.create_mitigation_plan(risk_id, steps)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/plans")
def list_plans():
    return mitigation_service.list_plans()

@router.get("/plans/{plan_id}")
def get_plan(plan_id: str):
    plan = mitigation_service.get_plan_by_id(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.post("/plans/{plan_id}/approve")
def approve_plan(plan_id: str):
    try:
        return mitigation_service.approve_plan(plan_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
