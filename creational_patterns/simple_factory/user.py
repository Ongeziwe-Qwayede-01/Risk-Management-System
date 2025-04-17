# from .user import An alyst, Admin, User

   
class User:
    def __init__(self, username):
        self.username = username

    def get_role(self):
        return "User"

class Admin(User):
    def get_role(self):
        return "Admin"

class Analyst(User):
    def get_role(self):
        return "Analyst"

class Analyst(User):
    def get_role(self):
        return "Analyst"

class Admin(User):
    def get_role(self):
        return "Admin"