from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from .models import Phone

        
class PhoneService:
    async def get_all_phone(self,session:AsyncSession):
        statement = select(Phone).order_by(desc(Phone.id))
        
        result = await session.exec(statement)
        return result.all()
    
    async def get_phone(self,id:int,session:AsyncSession):
        statement = select(Phone).where(Phone.id == id).order_by(desc(Phone.id))
        
        result = await session.exec(statement)
        
        return result.first()   