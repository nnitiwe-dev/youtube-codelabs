from typing import List

# Mock data
_items = [
    {"id": 1, "name": "Item One", "price": 9.99},
    {"id": 2, "name": "Item Two", "price": 19.99},
]


def list_items() -> List[dict]:
    return _items


def get_item(item_id: int) -> dict | None:
    return next((i for i in _items if i["id"] == item_id), None)