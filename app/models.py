from sqlalchemy import ForeignKey, Integer,String,Boolean,Column,DATETIME
from sqlalchemy.sql.expression import text
from .database import Base
from sqlalchemy.orm import relationship

class post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,nullable=False,server_default='True')
    created_at=Column(DATETIME,nullable=False,server_default=text('getutcdate()'))
    owner_id=Column(Integer,ForeignKey("Users.id",ondelete="CASCADE"),nullable=False)
    owner=relationship("user")

class user(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String(255),nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(DATETIME,nullable=False,server_default=text('getutcdate()'))

class vote(Base):
    __tablename__="votes"
    postid=Column(Integer,ForeignKey("posts.id",ondelete="NO ACTION"),primary_key=True)
    likedby_userid=Column(Integer,ForeignKey("Users.id",ondelete="NO ACTION"),primary_key=True)
    
