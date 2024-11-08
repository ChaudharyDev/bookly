from fastapi import APIRouter,status,Depends
from src.books.schemas import Book,BookResponse,BookUpdateModel
from typing import List,Optional
from fastapi.exceptions import HTTPException
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService



book_router = APIRouter()


@book_router.get('/',response_model=List[BookResponse])
async def get_books(id:Optional[str] = None,session:AsyncSession=Depends(get_session)):
    get_book=BookService()
    if id:
        result = await get_book.get_book(book_uid=id,session=session)
        return [result]
    else:
        return await get_book.get_all_book(session=session)



    
    
@book_router.post('/')
def create_book(book_data:List[Book]):
    pass

@book_router.delete('/')
def delete_book(id:int):
    pass


@book_router.patch('/')
def update(book_data:BookUpdateModel):
    pass
