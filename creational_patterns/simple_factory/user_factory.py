from creational_patterns.simple_factory.user import Admin, Analyst

class UserFactory:
    @staticmethod
    def create_user(role, username):
        if role == "Admin":
            return Admin(username)
        elif role == "Analyst":
            return Analyst(username)
        else:
            raise ValueError("Unknown role")
