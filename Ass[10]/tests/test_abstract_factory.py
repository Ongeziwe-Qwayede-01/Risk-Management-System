from creational_patterns.abstract_factory.report_factory import ReportFactory

def test_create_risk_report():
    factory = ReportFactory()
    report = factory.create_risk_report()
    assert report.generate() == "Risk report generated."

def test_create_compliance_report():
    factory = ReportFactory()
    report = factory.create_compliance_report()
    assert report.generate() == "Compliance report generated."
