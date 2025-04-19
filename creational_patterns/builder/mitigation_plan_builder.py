from .mitigation_plan import MitigationPlan

class MitigationPlanBuilder:
    def __init__(self):
        self.plan = MitigationPlan()

    def add_identification(self):
        self.plan.add_step("Identify Risk")
        return self

    def add_response(self):
        self.plan.add_step("Add Mitigation Response")
        return self

    def add_approval(self):
        self.plan.add_step("Approve Plan")
        return self

    def build(self):
        return self.plan

