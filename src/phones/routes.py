from fastapi import APIRouter,status,Depends
from src.phones.schemas import PhoneResponse
from typing import List,Optional
from fastapi.exceptions import HTTPException
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import PhoneService

phone_router = APIRouter()
ps=PhoneService()


@phone_router.get('/',response_model=List[PhoneResponse])
async def get_phones(id:Optional[int] = None,session:AsyncSession=Depends(get_session)):
    
    if id:
        result = await ps.get_phone(id=id,session=session)
        return [result]
    else:
        return await ps.get_all_phone(session=session)