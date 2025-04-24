from .base_repository import Repository
from src.risk import Risk  # adjust based on your file structure

class RiskRepository(Repository[Risk, str]):
    pass
