print("Script started")  # <-- debugging print
print("script again")
from creational_patterns.simple_factory.user_factory import UserFactory

user1 = UserFactory.create_user("Analyst", "Zanele")
user2 = UserFactory.create_user("Admin", "Thabo")

print(user1.username, "-", user1.get_role())  # Zanele - Analyst
print(user2.username, "-", user2.get_role())  # Thabo - Admin

# test_simple_factory_run.py