from sqlalchemy.orm import Session
from . import models, schemas

def get_contacts(db: Session):
    return db.query(models.Contact).all()

def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

def update_contact(db: Session, contact_id: int, updated: schemas.ContactCreate):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if contact:
        for key, value in updated.dict().items():
            setattr(contact, key, value)
        db.commit()
    return contact

def delete_contact(db: Session, contact_id: int):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact
