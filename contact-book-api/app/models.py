from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

contact_group = Table(
    'contact_group', Base.metadata,
    Column('contact_id', Integer, ForeignKey('contacts.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    groups = relationship("Group", secondary=contact_group, back_populates="contacts")

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    contacts = relationship("Contact", secondary=contact_group, back_populates="groups")
