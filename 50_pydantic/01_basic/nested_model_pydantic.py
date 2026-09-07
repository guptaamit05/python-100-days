from pydantic import BaseModel
from typing import  Optional


class Address(BaseModel):
    street:str
    city:str
    postal_code:str
    
class User(BaseModel):
    id:int
    name:str
    address: Address  ## Model Composition  useing  model as a type for address.
    


address = Address(street="124", city="Indore", postal_code='20234')
print( "Address == ", address)
user = User(id=2323, name="satish donge", address=address)

print(user)
print(user.address.city)

# ---- OR ---

user_data = {
    'id':2423,
    'name':"rajesh das",
    'address':{
        'city':"indore",
        'street':"323",
        'postal_code':'3434'
    }
}

usernew = User(** user_data)

print(usernew)
