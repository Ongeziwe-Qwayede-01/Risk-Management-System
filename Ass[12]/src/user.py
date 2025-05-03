import uuid

class User:
    def __init__(self, username, role):
        self.id = str(uuid.uuid4())
        self.username = username
        self.role = role