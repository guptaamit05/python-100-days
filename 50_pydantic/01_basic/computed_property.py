from pydantic import BaseModel, computed_field
from typing import Optional


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property   # so that is can be accessible outside ( ex: total_price without () )
    def total_price(self) -> float: 
        return self.price*self.quantity
    
    