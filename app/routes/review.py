from fastapi import APIRouter
from app.controllers.review_controller import router as review_router

router = APIRouter()
router.include_router(review_router, prefix="/reviews", tags=["Reviews"])
