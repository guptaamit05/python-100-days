from pydantic import BaseModel, field_validator, model_validator
from typing import Optional


class User(BaseModel):
    username: str
    
    @field_validator('username')
    def username_length(cls, v):
        if len(v)<4:
            raise ValueError("Username must be atleast 4 character long..")
        return v


class Signup(BaseModel):
    password: str
    confirm_password: str 
    
    @model_validator(mode='after')
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Password don't matched..")
        return self


user_pwd={
    'password':"123",
    'confirm_password':'123'
}
signup = Signup(**user_pwd)

print(signup)