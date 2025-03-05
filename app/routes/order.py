from fastapi import APIRouter
from app.controllers.order_controller import router as order_router

router = APIRouter()
router.include_router(order_router, prefix="/orders", tags=["Orders"])
