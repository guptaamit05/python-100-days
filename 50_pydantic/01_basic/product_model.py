from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool  = True

product1 = Product(id=1, name="Laptop", price=340.00, in_stock=True)
product2 = Product(id=2, name="Mini Laptop", price=340.23)

print(product1)
print(product2)