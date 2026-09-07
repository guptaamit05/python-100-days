from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: list[str] = []


model_config = ConfigDict(
    json_encoders={datetime: lambda x: x.strftime("%d-%m-%Y %H:%M:%S")}
)

user = User(
    id=22,
    name="satish das",
    email="ab@dd.com",
    created_at=datetime(2026, 3, 10, 15, 14, 20),
    address=Address(street="something", city="indore", zip_code="34234"),
    is_active=False,
    tags=["Premier User", "subscriber"],
)

# py_dict = user.model_dump()
py_dict = user.model_dump()
print("=" * 20)
print(py_dict)
print("=" * 20)

py_dict_json = user.model_dump_json(exclude=("address"))  ## exclude address from json
py_dict_json_include_address = user.model_dump_json(
    include=("address")
)  ## include only address
print(py_dict_json)
print("=" * 20)

print(py_dict_json_include_address)
print("=" * 20)
