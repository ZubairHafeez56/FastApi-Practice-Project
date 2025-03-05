from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.review_schema import ReviewCreate, ReviewResponse
from app.services.review_service import add_review, get_reviews_by_product
from app.config.database import SessionLocal
from app.utils.security import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{product_id}", response_model=ReviewResponse)
def post_review(product_id: int,
                review_data: ReviewCreate,
                db: Session = Depends(get_db),
                current_user = Depends(get_current_user)):
    review = add_review(db, user_id=current_user.id, product_id=product_id, rating=review_data.rating, comment=review_data.comment)
    return review

@router.get("/{product_id}", response_model=list[ReviewResponse])
def list_reviews(product_id: int,
                 db: Session = Depends(get_db)):
    return get_reviews_by_product(db, product_id=product_id)
