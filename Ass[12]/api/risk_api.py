# api/risk_api.py

from fastapi import APIRouter, Depends, HTTPException
from services.risk_service import RiskService
from repositories.inmemory.in_memory_risk_repository import InMemoryRiskRepository

router = APIRouter()

risk_service = RiskService(InMemoryRiskRepository())

@router.post("/risks")
def create_risk(description: str, severity: str, likelihood: str):
    try:
        return risk_service.create_risk(description, severity, likelihood)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/risks")
def get_all_risks():
    return risk_service.get_all_risks()

@router.get("/risks/{risk_id}")
def get_risk_by_id(risk_id: str):
    risk = risk_service.get_risk_by_id(risk_id)
    if not risk:
        raise HTTPException(status_code=404, detail="Risk not found")
    return risk

@router.put("/risks/{risk_id}")
def update_risk(risk_id: str, description: str, severity: str, likelihood: str):
    try:
        return risk_service.update_risk(risk_id, description, severity, likelihood)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/risks/{risk_id}")
def delete_risk(risk_id: str):
    return risk_service.delete_risk(risk_id)
