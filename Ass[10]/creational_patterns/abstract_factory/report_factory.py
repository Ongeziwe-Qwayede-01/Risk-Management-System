from .compliance_report import ComplianceReport
from .risk_report import RiskReport

class ReportFactory:
    def create_risk_report(self):
        return RiskReport()

    def create_compliance_report(self):
        return ComplianceReport()