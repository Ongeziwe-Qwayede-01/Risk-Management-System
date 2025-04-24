from factories.repository_factory import RepositoryFactory
from src.risk import Risk

def main():
    print("📊 RMS Repository Pattern Demo\n")

    # Get the in-memory repository using factory
    risk_repo = RepositoryFactory.get_risk_repository()

    # Create a risk object
    risk = Risk("R001", "Data Leak", "High", "Likely")
    risk_repo.save(risk)

    # Retrieve it by ID
    fetched = risk_repo.find_by_id("R001")

    if fetched:
        print(f"✅ Retrieved Risk:\nID: {fetched.risk_id}, Desc: {fetched.description}, Severity: {fetched.severity}, Likelihood: {fetched.likelihood}")
    else:
        print("❌ Risk not found.")

if __name__ == "__main__":
    main()
