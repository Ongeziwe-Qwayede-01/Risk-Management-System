from repositories.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def create(self, item):
        self.users[item.id] = item
        return item

    def get(self, item_id):
        return self.users.get(item_id)

    def list(self):
        return list(self.users.values())

    def delete(self, item_id):
        return self.users.pop(item_id, None)