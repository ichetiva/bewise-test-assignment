from typing import Generic, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base

Model = TypeVar("Model", Base, Base)


class BaseDAO(Generic[Model]):
    def __init__(self, model: Type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get(self, for_update: bool = False, **kwargs) -> Model | None:
        stmt = select(self.model).filter_by(**kwargs)
        if for_update:
            stmt = stmt.with_for_update()
        result = await self.session.scalar(stmt)
        return result

    async def get_list(self, **kwargs) -> list[Model]:
        stmt = select(self.model).filter_by(**kwargs)
        result = await self.session.scalars(stmt)
        return result.all()
