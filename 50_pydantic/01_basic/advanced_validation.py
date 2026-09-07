from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime


class Person(BaseModel):
    name: str
    last_name: str

    @field_validator("name", "last_name")
    def name_must_capitalize(cls, value):
        if not value.istitle():
            raise ValueError("Name must be capitalize ")
        return value


person = Person(name="Amit", last_name="Das")
print(person)


class User(BaseModel):
    email: str

    @field_validator(
        "email", mode="before"
    )  # mode: Specifies whether to validate the fields before or after validation.
    def normalize_email(cls, value):
        return value.lower().strip()


user = User(email="SatishRte@gmail.com")
print(user)


class DateV(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def check_start_date_should_less(value):
        if value.start_date >= value.end_date:
            raise ValueError("Start date should be less than end date ")
        return value
