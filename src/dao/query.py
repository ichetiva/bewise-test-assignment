from sqlalchemy.ext.asyncio import AsyncSession

from dao.base import BaseDAO
from models import Query


class QueryDAO(BaseDAO[Query]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Query, session)

    async def create(self) -> Query:
        q = Query()
        self.session.add(q)
        await self.session.flush()
        return q
