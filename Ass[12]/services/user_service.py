from repositories.user_repository import UserRepository
from src.user import User
from uuid import uuid4

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, username, role):
        if not username or not role:
            raise ValueError("Username and role must be provided")

        user = User(
            id=str(uuid4()),
            username=username,
            role=role
        )
        self.repository.save(user)
        return user

    def get_user(self, user_id):
        return self.repository.find_by_id(user_id)

    def list_users(self):
        return self.repository.list_all()

    def delete_user(self, user_id):
        self.repository.delete(user_id)
        return True
