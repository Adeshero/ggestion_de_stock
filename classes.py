import json
from enum import Enum
import bcrypt 


#creer les enumérations

class type_db(Enum):
    user="user"
    stockage="stockage"
    supplier="supplier"

#classe pour retourner la db

def get_db(type:type_db =type_db.user):
    
    with open('user_db.json','r') as f:
        content = json.load(f)
    
    if type == type_db.user:
        return content.get("users",[])
    


def valide_user(userName:str):
    
    data=get_db(type_db.user)
    for user in data:
        if user.get("firstName") == userName:
            return user 
    return None


            
        
    
            

    
        

def checkpw(password :bytes,passphrase:bytes):
    if password.decode() == passphrase.decode():
        return True 
    else:
        return False
