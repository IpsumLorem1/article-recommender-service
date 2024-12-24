from fastapi import APIRouter
from src.api.routes import predict

router = APIRouter()
router.include_router(predict.router, tags=["search"])
