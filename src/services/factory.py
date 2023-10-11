from dao import DAOFactory

from services.query import QueryService
from services.question import QuestionService
from services.question_integration import QuestionIntegrationService


class ServicesFactory:
    def __init__(self, daos: DAOFactory) -> None:
        self.daos = daos

    @property
    def query_service(self) -> QueryService:
        return QueryService(self.daos)

    @property
    def question_service(self) -> QuestionService:
        return QuestionService(self.daos, self)

    @property
    def question_integration_service(self) -> QuestionIntegrationService:
        return QuestionIntegrationService()
