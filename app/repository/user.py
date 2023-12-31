from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from .. import models, schemas
from .. import schemas, models, database, models, hashing
from ..repository import user

def create(db: Session, request: schemas.GetUser):
    new_user = models.User(name = request.name, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'User with {id} was not found')
    
    return user