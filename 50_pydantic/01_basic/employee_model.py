from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    user_id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Harish Das",
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=1000, title="Should be greater than 1000")


user = {"user_id": 12, "name": "atare", "salary": 1000}

try:
    userprint = User(**user)
    print(userprint)
except Exception as e:
    print("Error: ", e)


class User(BaseModel):
    email: str = Field(..., ge=10)
    phone: str = Field(..., regex=r"")
    age: int = Field(..., ge=10, le=80, description="Age in Years")
    discount: float = Field(ge=0, le=100, description="Discount Percentage..")
