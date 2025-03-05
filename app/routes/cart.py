from fastapi import APIRouter
from app.controllers.cart_controller import router as cart_router

router = APIRouter()
router.include_router(cart_router, prefix="/cart", tags=["Cart"])
