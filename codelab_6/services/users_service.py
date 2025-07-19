from typing import List

# Mock data
_users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]


def list_users() -> List[dict]:
    return _users


def get_user(user_id: int) -> dict | None:
    return next((u for u in _users if u["id"] == user_id), None)