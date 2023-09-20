from .routes import posts,users,auth,votes
from fastapi import FastAPI
from . import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware



#models.Base.metadata.create_all(bind=engine)
#alembic handles this now 

app=FastAPI()

origins =["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(posts.router)

app.include_router(users.router)

app.include_router(auth.router)

app.include_router(votes.router)

@app.get("/")
async def root():
    return {"message":"hello world by Karan"}

 #using in memory method with api
'''postdict=[{"title":"title1","content":"content1","rating":5,"id":1},
          {"title":"title3","content":"content3","rating":7,"id":3},
          {"title":"title2","content":"content2","rating":4,"id":2}]

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.post("/createposts")
def saveposts(payload:dict = Body(...)):
    print(payload)
    return {"new_post":f"title:{payload['title']} content:{payload['content']}"}

@app.post("/createnewposts")
def saveposts(newpost:post = Body(...)):
    print(newpost)
    print(newpost.dict())
    return {"message":"success"}'''




# using  pyodbc

''''def getposts(id):
     for post in postdict:
        if post["id"]==id:
            return post
        
def getopostindex(id):
     for i,post in enumerate(postdict):
        if post["id"]==id:
            return i'''
            

'''@app.get("/posts")
def getallposts():
    cursor.execute("select * from posts")
    columns = [column[0] for column in cursor.description]
    print(columns)
    rows=cursor.fetchall()
    # Convert rows to a list of dictionaries
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    
    print(results)
    return{"data":results}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def saveposts(post:post):
    cursor.execute("insert into posts (title,content,published) OUTPUT INSERTED.* values (?, ?, ?) ",post.title,post.content,post.published)
    column = [column[0] for column in cursor.description]
    row=cursor.fetchone()
    cursor.commit()
    result=[]
    result.append(dict(zip(column,row)))
    return {"Inserted Data":result}

@app.get("/posts/{id}")
def getallposts(id:int):
    cursor.execute("select * from posts where id=?",str(id))
    #post=getposts(id)
    row=cursor.fetchone()
    if row is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id:{id} was not found"
        )
    column = [column[0] for column in cursor.description]
    results = []
    results.append(dict(zip(column, row)))
    return {"post":results}



@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("delete  from posts OUTPUT Deleted.* where id=? ",str(id))
    row=cursor.fetchone()
    cursor.commit()
    
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"no such resource found at id:{id}") 
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

    
@app.put("/posts/{id}")
def update_post(id:int,post:post):
    
     cursor.execute("UPDATE posts SET title = ?, content = ?, published=? OUTPUT inserted.* WHERE id = ?",post.title,post.content,post.published,str(id))
     column=[column[0] for column in cursor.description]
     row=cursor.fetchone()
     if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"no such resource fount at id:{id}")
     cursor.commit()
     result=[]
     result.append(dict(zip(column,row)))
     
     return{"updated_post":result}'''

