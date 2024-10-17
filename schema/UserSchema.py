from pydantic import BaseModel
from typing import Optional

# Pydantic model for serialization
class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    role: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

    class Config:
        orm_mode = True 

class UserCreateSchema(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    role: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

    class Config:
        orm_mode = True 
