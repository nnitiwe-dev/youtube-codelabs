from fastapi import APIRouter, HTTPException
from services.users_service import get_user, list_users
from pydantic import BaseModel, Field

class User(BaseModel):
    """
    Represents a user in the system.
    """
    id: int = Field(..., example=1, description="Unique identifier for the user")
    name: str = Field(..., example="Alice", description="Full name of the user")
    email: str = Field(..., example="alice@example.com", description="User's email address")

router = APIRouter()

@router.get(
    "/",
    response_model=list[User],
    summary="List all users",
    description="Retrieve a list of all registered users.",
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": [
                        {"id":1, "name":"Alice", "email":"alice@example.com"}
                    ]
                }
            }
        }
    }
)
async def read_users():
    """
    Endpoint to fetch all users.
    """
    return list_users()

@router.get(
    "/{user_id}",
    response_model=User,
    summary="Get a single user",
    description="Fetch detailed information about a user by ID.",
    responses={
        200: {"description": "User found"},
        404: {"description": "User not found"}
    }
)
async def read_user(user_id: int):
    """
    Get user by ID.
    - **user_id**: integer ID of the user to retrieve
    """
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user