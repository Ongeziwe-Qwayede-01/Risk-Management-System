from repositories.inmemory.in_memory_risk_repository import InMemoryRiskRepository

class RepositoryFactory:
    @staticmethod
    def get_risk_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryRiskRepository()
        else:
            raise ValueError("Unsupported storage type")
