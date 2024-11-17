from pydantic import BaseModel
from typing import Optional,Union
    
    
class PhoneResponse(BaseModel):
    id:int
    name : str
    price : str
    img : str