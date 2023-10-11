from sqlalchemy import Column, Integer

from models.base import Base


class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True)
