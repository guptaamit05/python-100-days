from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# input_data = {'id':1010, 'name':"Chandan", 'is_active':3}  # Through an error  Input should be a valid boolean,
input_data = {'id':1010, 'name':"Chandan", 'is_active':True}
user = User(**input_data)
# print(user)