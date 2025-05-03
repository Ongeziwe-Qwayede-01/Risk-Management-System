from repositories.risk_repository import RiskRepository

class InMemoryRiskRepository(RiskRepository):
    def __init__(self):
        self.risks = {}

    def create(self, item):
        self.risks[item.id] = item
        return item

    def get(self, item_id):
        return self.risks.get(item_id)

    def list(self):
        return list(self.risks.values())

    def delete(self, item_id):
        return self.risks.pop(item_id, None)
