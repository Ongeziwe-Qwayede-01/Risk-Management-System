import uuid

class MitigationPlan:
    def __init__(self, risk_id, steps):
        self.id = str(uuid.uuid4())
        self.risk_id = risk_id
        self.steps = steps
        self.approved = False

    def approve(self):
        self.approved = True
