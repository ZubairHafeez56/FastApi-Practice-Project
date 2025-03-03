from fastapi import APIRouter
from app.controllers.product_controller import router as product_router

router = APIRouter()
router.include_router(product_router, prefix="/product", tags=["Products"])
