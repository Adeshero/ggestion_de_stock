from pydantic import BaseModel
from datetime import datetime 

class User(BaseModel):
    id: int 
    name:str
    passphrase:str|None=None
    signup_ts:datetime | None=None

class userProfile(BaseModel):
    id :int 
    firstName:str
    lastName:str
    passphrase:str #attention mec
    
class stockage(BaseModel):
    id:int
    name:str 
    description:str|None= None
    supplier:str
    
class transation(BaseModel):
    id:int
    title:str
    description:str
    makeAt:datetime 
    
