from fastapi import FastAPI
from classes import valide_user,checkpw
from models import *
import uuid

app = FastAPI()

@app.get("/")
def mainPage():
    return("Hello world ")

@app.post("/user/login")
def login(userName:str ="jordane", userPassword:str =None):
    
   if valide_user(userName) ==None :
        return "user not found"
   else:
       user = valide_user(userName)
       if checkpw(userPassword.encode(),user.get("passphrase").encode()):
           return f"user {userName} succefully identify "
       else :
           return "password error"
           
# tres belles routes mais la validation est assez légère. Utilise pydantics
            
        
    
