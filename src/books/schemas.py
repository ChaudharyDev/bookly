from pydantic import BaseModel
from typing import Optional,Union

class Book(BaseModel):
    # id : int
    title : str
    publisher : str
    author : str
    published_date : str
    page_count : Optional[int] = None
    language : str
    
class BookResponse(BaseModel):
    id : int
    title : str
    publisher : str
    author : str
    published_date : str
    page_count : Union[int,None]
    language : str
    
class BookUpdateModel(BaseModel):
    id : int
    title : Optional[str] = None
    publisher : Optional[str] = None
    author : Optional[str] = None
    published_date : Optional[str] = None
    page_count : Union[int,None]
    language : Optional[str] = None
    
    
