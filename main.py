from enum import Enum
from fastapi import FastAPI, UploadFile, File
import os


app=FastAPI()


curentdir=os.getcwd()
folderexist=lambda folder_name :folder_name in os.listdir(curentdir)






class Privilage(str,Enum):
    ADMIN="admin"
    USER="user"

@app.get("/")
def main():
    return {"message" :"hello world "}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/access/{prev}")
def user_previlage(prev:Privilage):
    if prev is Privilage.ADMIN:
        return {"User_previlage":Privilage.ADMIN}
    else :
        return {"messgae ":"not allowed to use resorse "}

@app.post("/user/photo/")
async def uploadPhoto(file:UploadFile=File(...)):
    Fexist=folderexist("uploade") 

    print(f"result:{Fexist}")
    if not file or not file.filename:
        return {"message ":"no file uploded ."}
    if  not Fexist:
        os.mkdir("uploade")
    with open (f"uploade/{file.filename}","wb") as f :
        content=await file.read()
        f.write(content)
    return {"file_name ":file.filename , "content_type":file.content_type }
    

