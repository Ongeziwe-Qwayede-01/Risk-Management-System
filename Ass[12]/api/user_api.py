from fastapi import APIRouter, HTTPException
from services.user_service import UserService
from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository

router = APIRouter()

user_service = UserService(InMemoryUserRepository())

@router.post("/users")
def create_user(username: str, role: str):
    try:
        return user_service.create_user(username, role)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users")
def list_users():
    return user_service.list_users()

@router.get("/users/{user_id}")
def get_user(user_id: str):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    return user_service.delete_user(user_id)
