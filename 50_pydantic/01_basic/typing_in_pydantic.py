from pydantic import BaseModel
from typing import Optional


class Cart(BaseModel):
    user_id: int
    items: list[str]
    quantity: dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


cart_data = {
    'user_id':1,
    'items':['laptop', 'mouse', 'screen', 'speaker'],
    'quantity':{'laptop':2, 'mouse':34, 'screen':122, 'speaker':34},
}

cart = Cart(**cart_data)

print(cart)