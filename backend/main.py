from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.router import router as api_router


def get_app() -> FastAPI:
    """
    Инициализация приложения FastAPI.
    """
    fastapi_app = FastAPI(
        title="Article Search Service",
        version="1.0.0",
        debug=True,
        description="Service for searching similar articles by user input",
    )

    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

    fastapi_app.include_router(api_router, prefix="/api")

    return fastapi_app


app = get_app()
