from dao import DAOFactory
from models import Query


class QueryService:
    def __init__(self, daos: DAOFactory) -> None:
        self.daos = daos

    async def create(self) -> Query:
        query = await self.daos.query_dao.create()
        await self.daos.session.commit()
        return query
