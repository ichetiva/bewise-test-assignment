from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies.database import get_session
from services import ServicesFactory
from dao import DAOFactory


async def get_services(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> ServicesFactory:
    daos = DAOFactory(session)
    services = ServicesFactory(daos)
    return services
