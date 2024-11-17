from sqlmodel import SQLModel,Field,Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
    
class Phone(SQLModel, table=True):
    __tablename__="phones"
    id: int = Field(primary_key=True, index=True)
    name : str
    price : str
    img : str    
    
    