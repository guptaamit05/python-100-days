from pydantic import BaseModel
from typing import Optional, Union


class Address(BaseModel):
    city: str
    pin_code: str
    street: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None  ## Address optional nested model


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None  ## Company optional nested model


class TextContent(BaseModel):
    type: str = "text"
    content: str


class ImageContent(BaseModel):
    type: str = "image"
    url: str
    all_text: str


class Article(BaseModel):
    type: str
    sections: list([Union(TextContent, ImageContent)])  ## mixed data types

# =======================================================
## Deeply nested Architecture....

class Country(BaseModel):
    name:str
    code:str

class State(BaseModel):
    name:str
    country:Country

class City(BaseModel):
    name:str
    state:State
    
class AddresssNew(BaseModel):
    country:Country
    city:City
    state:State
    pin_code:str

class Organization(BaseModel):
    name:str
    head_quater: AddresssNew
    branches:list(AddresssNew) = None
    



