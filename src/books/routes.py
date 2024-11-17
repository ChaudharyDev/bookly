from fastapi import APIRouter,status,Depends
from src.books.schemas import Book,BookResponse,BookUpdateModel,BookCreateModel
from typing import List,Optional
from fastapi.exceptions import HTTPException
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService
import uuid



book_router = APIRouter()
bs=BookService()

@book_router.get('/',response_model=List[BookResponse])
async def get_books(id:Optional[str] = None,session:AsyncSession=Depends(get_session)):
    
    if id:
        result = await bs.get_book(book_uid=id,session=session)
        return [result]
    else:
        return await bs.get_all_book(session=session)



    
    
@book_router.post('/')
async def create_book(book_data:List[BookCreateModel],session:AsyncSession=Depends(get_session)):
    for book in book_data :
        bs=BookService()
        print(book)
        # book.uuid=uuid.UUID()
        # book.created_at=
        rs= await bs.create_book(book,session)
        
    return 'created'   

@book_router.delete('/')
def delete_book(id:int):
    pass


@book_router.patch('/')
def update(book_data:BookUpdateModel):
    pass
