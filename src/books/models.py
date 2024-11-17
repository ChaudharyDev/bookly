from sqlmodel import SQLModel,Field,Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid




class Book(SQLModel, table=True):
    __tablename__="books"
    
    uid : uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
           pg.UUID(as_uuid=True),
           primary_key=True,
           nullable=False
        )
    )
    title : str
    publisher : str
    author : str
    published_date : str
    page_count : int
    language : str
    created_at : datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    update_at : datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    
    
    def __repr__(self):
        return f"<Book {self.title}>"
    