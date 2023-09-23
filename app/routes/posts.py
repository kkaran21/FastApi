from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from .. import models,schemas,oauth2
from ..database import  get_db
from typing import List, Optional
from fastapi import Depends,Response,status,HTTPException,APIRouter,UploadFile


router=APIRouter(
    prefix="/posts",
    tags=["Posts"]

)

DIRECTORY="D:\\apimedia"

# using orm sqlalchemy
@router.get("/",response_model=list[schemas.postResponseV2])
async def root(db: Session = Depends(get_db),limit:Optional[int]=10,search:Optional[str]="",skip:Optional[int]=0):
    #posts=db.query(models.post).filter(models.post.title.contains(search)).limit(limit).offset(skip).all()
    #posts = db.query(models.post).filter(models.post.title.contains(search)).order_by(desc(models.post.created_at)).limit(limit).offset(skip).all()
    subquery = (
    db.query(
     models.post.id.label('id'),
        func.count(models.vote.postid).label('likes')
    )
    .outerjoin(models.vote, models.post.id == models.vote.postid)
    .group_by(models.post.id)
    .subquery()
    )

# Create the main query using the alias
    main_query = (
    db.query(models.post, subquery.c.likes)
    .join(subquery, models.post.id == subquery.c.id)
    ).filter(models.post.title.contains(search)).order_by(desc(models.post.created_at)).limit(limit).offset(skip).all() 
    posts=main_query

    return posts


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.postResponse)
def saveposts(post:schemas.postCreate,db:Session=Depends(get_db),verify_token:dict=Depends(oauth2.verify_access_token)):
    
    new_post=models.post(**post.dict(),owner_id=verify_token.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}",response_model=schemas.postResponse)
def getallposts(id:int,db: Session = Depends(get_db),verify_token:dict=Depends(oauth2.verify_access_token)):
    results=db.query(models.post).filter(models.post.id==id).first()   
    if results is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id:{id} was not found"
        )

    return results


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),verify_token:dict=Depends(oauth2.verify_access_token)):
    result = db.query(models.post).filter(models.post.id==id)
   
    if result.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"no such resource found at id:{id}") 
    
    if result.first().owner_id != verify_token.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not Authorised to perform requested action") 
    
    result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.postResponse)
def update_post(id:int,post:schemas.postBase,db:Session=Depends(get_db),verify_token:dict=Depends(oauth2.verify_access_token)):
    
     result=db.query(models.post).filter(models.post.id==id)
     if result.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"no such resource fount at id:{id}")
     
     if result.first().owner_id != verify_token.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not Authorised to perform requested action") 
     result.update(post.dict(),synchronize_session=False)
     db.commit()
     
     return result.first()


@router.post("/upload")
async def upload(file:UploadFile,db:Session=Depends(get_db)):
    contents=await file.read()
    full_path = f"{DIRECTORY}\{file.filename}"
    with open(full_path,"wb+") as f:
        f.write(contents)
    db.query(models.post)
        
    return {'filename':'uploaded successfully'}
