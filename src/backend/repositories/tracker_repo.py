from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.models.canaries import Canaries
from backend.models.visits import Visits

async def get_canary(session: AsyncSession, token: str):
    query = (select(Canaries).where(Canaries.token == token))
    result = await session.execute(query)

    return result.one_or_none()

async def add_visit(session: AsyncSession, visit: Visits):
    session.add(visit)
    await session.commit()
    await session.refresh()

    return visit