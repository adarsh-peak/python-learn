from pydantic import BaseModel
from typing import Optional

# Pydantic model for serialization
class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True 

class UserCreateSchema(BaseModel):
    name: str
    email: str
    id: Optional[int] = None

    class Config:
        orm_mode = True 
