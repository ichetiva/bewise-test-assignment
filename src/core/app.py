from fastapi import FastAPI

from api import router as api_router


def get_application() -> FastAPI:
    app = FastAPI()

    app.include_router(api_router)

    return app
