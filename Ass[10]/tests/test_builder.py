from creational_patterns.builder.mitigation_plan_builder import MitigationPlanBuilder

def test_mitigation_plan():
    builder = MitigationPlanBuilder()
    plan = builder.add_identification().add_response().add_approval().build()
    assert plan.show_plan() == "Identify Risk -> Add Mitigation Response -> Approve Plan"
