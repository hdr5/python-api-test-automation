from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr


app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: EmailStr


users = [
    {"id": 1, "name": "David", "email": "david@example.com"},
    {"id": 2, "name": "Sarah", "email": "sarah@example.com"}
]


@app.get("/users")
def get_users():
    return users


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    return new_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )