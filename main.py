import sys
import os
sys.path.append(os.path.abspath(".."))

from creational_patterns.simple_factory.user_factory import UserFactory
from creational_patterns.factory_method.payment_processor import NotificationProcessor
from creational_patterns.factory_method.notification_base import NotificationProcessor
from creational_patterns.abstract_factory.report_factory import ReportFactory
from creational_patterns.builder.mitigation_plan_builder import MitigationPlanBuilder
from creational_patterns.prototype.alert_cache import AlertCache
from creational_patterns.singleton.database_connection import DatabaseConnection

def main():
    print("Risk Management System – Pattern Demo\n")

    # Simple Factory
    user = UserFactory.create_user("Admin", "Thabo")
    print(f"User created: {user.username} – Role: {user.get_role()}")

    # Factory Method
    processor = NotificationProcessor.create_processor("email")
    processor.send_alert("New risk identified!")

    # Abstract Factory
    report_factory = ReportFactory()
    print(report_factory.create_compliance_report().generate())

    # Builder
    plan = MitigationPlanBuilder().add_identification().add_response().add_approval().build()
    print("Mitigation Plan:", plan.show_plan())

    # Prototype
    alert_cache = AlertCache()
    alert_cache.load()
    alert = alert_cache.get_alert("critical")
    print(f"Cloned Alert: [{alert.severity}] {alert.message}")

    # Singleton
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print("Singleton DB Check:", db1 is db2, "–", db1.get_connection())

if __name__ == "__main__":
    main()
