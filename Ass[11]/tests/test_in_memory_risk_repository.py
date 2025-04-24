import unittest
from repositories.inmemory.in_memory_risk_repository import InMemoryRiskRepository
from src.risk import Risk

class TestInMemoryRiskRepository(unittest.TestCase):
    def test_save_and_find(self):
        repo = InMemoryRiskRepository()
        risk = Risk("R1", "Cyber Threat", "High", "Likely")
        repo.save(risk)
        self.assertEqual(repo.find_by_id("R1"), risk)

    def test_delete(self):
        repo = InMemoryRiskRepository()
        risk = Risk("R2", "Data Breach", "Medium", "Possible")
        repo.save(risk)
        repo.delete("R2")
        self.assertIsNone(repo.find_by_id("R2"))

if __name__ == "__main__":
    unittest.main()
