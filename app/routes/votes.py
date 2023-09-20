from fastapi import Depends,Response,status,HTTPException,APIRouter
from .. import schemas,database,oauth2,models
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.vote,db:Session=Depends(database.get_db),verify_token:dict=Depends(oauth2.verify_access_token)):

    post_exist=db.query(models.post).filter(models.post.id==vote.postid).first()

    if not post_exist:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {vote.postid} does not exist")

    db_query=db.query(models.vote).filter(models.vote.likedby_userid==verify_token.id,models.vote.postid==vote.postid)
    vote_found=db_query.first()

    if vote.dir==1:
        if vote_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="You have already liked the post")
        like=models.vote(postid=vote.postid,likedby_userid=verify_token.id)
        db.add(like)
        db.commit()
        return {"message":"You have liked the post"}
    
    else:
        if not vote_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="how will you unlike if you haven't liked the post in the firt place dummy")
        db_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"you have removed your like"}


    
