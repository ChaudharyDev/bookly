from fastapi import APIRouter,status,Depends
from pydantic import BaseModel
from src.books.schemas import Book,BookResponse,BookUpdateModel
# from src.books.book_data import books
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
    # if id:
    #     for book in books:
    #         if book['id']== id:
    #             return [book]
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
        # return {"error":f"not found id:{id}"}
                
    # return books



    
    
@book_router.post('/')
def create_book(book_data:List[Book]):
    print(book_data)
    
    max_element = books[0]['id']
    for book in books:
        if max_element < book['id']:
            max_element=book['id']
    # max_element = max_element  
    temp_list = []
    for book in book_data:
        new_book = book.model_dump()
        new_book['id'] = max_element+1
        max_element=max_element+1
        temp_list.book_routerend(new_book)
    books.extend(temp_list)

    # new_book = {
    #         "id":max_element,
    #         "title":book_data.title,
    #         "publisher":book_data.publisher,
    #         "author":book_data.author,
    #         "published_date":book_data.published_date,
    #         "page_count":book_data.page_count,
    #         "language":book_data.language,
    #         },
    
    # new_book = book_data.model_dump()
    # new_book['id'] = max_element
    # books.book_routerend(new_book)
    
    return temp_list

@book_router.delete('/')
def delete_book(id:int):
    for index,book in enumerate(books):
        if book['id'] == id:
            books.pop(index)
            return {"message":"deleted succesful"}
    return {"message":"id not found"}


@book_router.patch('/')
def update(book_data:BookUpdateModel):
    update_book = book_data.model_dump(exclude_unset=True)
    
    for index,book in enumerate(books):
        if book['id'] == update_book['id']:
            book['title'] = update_book.get('title',book['title'])
            book['publisher'] = update_book.get('publisher',book['publisher'])
            book['author'] = update_book.get('author',book['author'])
            book['published_date'] = update_book.get('published_date',book['published_date'])
            book['page_count'] = update_book.get('page_count',book['page_count'])
            book['language'] = update_book.get('language',book['language'])
            return {"message":"updated succesful"}
    return {"message":"id not found"}
            
