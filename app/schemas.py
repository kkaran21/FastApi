from datetime import datetime
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:int
    email:EmailStr
    
class userCreate(BaseModel):
    email:EmailStr
    password:str

class userResponse(BaseModel):
    email:EmailStr
    id:int
    class Config:   #is required while using an orm 
        orm_mode=True

class userLogin(BaseModel):
    email:EmailStr
    password:str



class postBase(BaseModel):
    title:str
    content:str
    published:bool=True
    
   
class postCreate(postBase):
    pass   #pass means null statement that is not executed

class postResponse(postBase):
    created_at:datetime
    owner_id:int
    
    owner:userResponse
    
    class Config:   #is required while using an orm 
        orm_mode=True

class postResponseV2(BaseModel):
    post:postResponse
    likes:int
    
    class Config:   #is required while using an orm 
        orm_mode=True


class vote(BaseModel):
    postid:int
    dir:bool

