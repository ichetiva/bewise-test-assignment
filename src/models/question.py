from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from models.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    text = Column(String(512), nullable=False)
    answer = Column(String(128), nullable=False)
    created_at = Column(DateTime, nullable=False)

    query_id = Column(Integer, ForeignKey("queries.id", ondelete="CASCADE"))
