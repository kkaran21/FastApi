from sqlalchemy.orm import Session
from .. import models,schemas,utils
from ..database import  get_db
from fastapi import Depends,status,HTTPException,APIRouter

router=APIRouter(
    prefix="/users",
    tags=["Users"]

)

#add an exception for unique email constraint
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.userResponse)
def createUser(user:schemas.userCreate,db:Session=Depends(get_db)):

    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user=models.user(**user.dict())
    Is_duplicate_email=db.query(models.user).filter(models.user.email==new_user.email).first()
    if Is_duplicate_email is not None:
          raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"User with email:{Is_duplicate_email.email} already exists"
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",status_code=status.HTTP_404_NOT_FOUND,response_model=schemas.userResponse)
def getuserbyid(id:int,db:Session=Depends(get_db)):
    fetchuser=db.query(models.user).filter(models.user.id==id).first()
    if fetchuser is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id:{id} was not found"
        )
    return fetchuser