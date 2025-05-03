from repositories.mitigation_plan_repository import MitigationPlanRepository
from src.mitigation_plan import MitigationPlan
from src.risk import Risk
from uuid import uuid4

class MitigationPlanService:
    def __init__(self, repository: MitigationPlanRepository, risk_repository):
        self.repository = repository
        self.risk_repository = risk_repository

    def create_mitigation_plan(self, risk_id, steps):
        risk = self.risk_repository.find_by_id(risk_id)
        if not risk:
            raise ValueError("Associated risk not found")

        plan = MitigationPlan(
            id=str(uuid4()),
            risk_id=risk_id,
            steps=steps,
            status="Pending"
        )
        self.repository.save(plan)
        return plan

    def get_plan_by_id(self, plan_id):
        return self.repository.find_by_id(plan_id)

    def list_plans(self):
        return self.repository.list_all()

    def approve_plan(self, plan_id):
        plan = self.repository.find_by_id(plan_id)
        if not plan:
            raise ValueError("Plan not found")

        plan.status = "Approved"
        self.repository.save(plan)
        return plan
