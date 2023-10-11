from fastapi import APIRouter

from api.questions import router as questions_router

router = APIRouter(prefix="/api")

router.include_router(questions_router)
