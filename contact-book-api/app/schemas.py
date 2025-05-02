from pydantic import BaseModel
from typing import List, Optional

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    class Config:
        orm_mode = True

class ContactBase(BaseModel):
    name: str
    email: Optional[str]
    phone: Optional[str]

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    groups: List[Group] = []
    class Config:
        orm_mode = True
