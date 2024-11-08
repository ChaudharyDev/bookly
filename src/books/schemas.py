from pydantic import BaseModel
from typing import Optional,Union
import uuid 
from datetime import datetime

class Book(BaseModel):
    uid : uuid.UUID
    title : str
    publisher : str
    author : str
    published_date : str
    page_count : Optional[int] = None
    language : str
    created_at : datetime
    update_at : datetime
    
class BookResponse(BaseModel):
    uid : uuid.UUID
    title : str
    publisher : str
    author : str
    published_date : str
    page_count : Union[int,None]
    language : str
 
 
class BookCreateModel(BaseModel):
    title : str
    publisher : str
    author : str
    published_date : datetime
    page_count : int
    language : str
    
class BookUpdateModel(BaseModel):
    uid : int
    title : Optional[str] = None
    publisher : Optional[str] = None
    author : Optional[str] = None
    published_date : Optional[str] = None
    page_count : Union[int,None]
    language : Optional[str] = None
    
    
