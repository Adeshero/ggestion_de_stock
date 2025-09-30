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
    supplier:str # Tu as oubblié la quantité (très important dans la logique de gestion de stock)
    
class transation(BaseModel):
    id:int
    title:str
    description:str
    makeAt:datetime # Là tu as oublié de mentionner le user qui a fait la transaction
    
