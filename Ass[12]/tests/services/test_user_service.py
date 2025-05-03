from services.user_service import UserService
from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository

def test_create_user():
    repo = InMemoryUserRepository()
    service = UserService(repo)
    user = service.create_user("Thabo", "Admin")
    assert user.username == "Thabo"
