from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import user

router = APIRouter(
    prefix = '/user',
    tags = ['Users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.GetUser)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(db, request)

@router.get('/{id}', response_model=schemas.GetUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)