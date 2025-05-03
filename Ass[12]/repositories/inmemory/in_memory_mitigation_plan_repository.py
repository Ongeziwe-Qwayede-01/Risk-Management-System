from repositories.mitigation_plan_repository import MitigationPlanRepository

class InMemoryMitigationPlanRepository(MitigationPlanRepository):
    def __init__(self):
        self.plans = {}

    def create(self, item):
        self.plans[item.id] = item
        return item

    def get(self, item_id):
        return self.plans.get(item_id)

    def list(self):
        return list(self.plans.values())

    def delete(self, item_id):
        return self.plans.pop(item_id, None)
