from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.canaries import Canaries

async def get_canary(session: AsyncSession, token: str):
    query = (select(Canaries).where(Canaries.token == token))
    result = await session.execute(query)

    return result.one_or_none()