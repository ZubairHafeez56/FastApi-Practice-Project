from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.cart_schema import CartItemCreate, CartItemResponse
from app.services.cart_service import add_to_cart, remove_from_cart, get_cart_items
from app.config.database import SessionLocal
from app.utils.security import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CartItemResponse)
def add_item_to_cart(item: CartItemCreate,
                     db: Session = Depends(get_db),
                     current_user = Depends(get_current_user)):
    return add_to_cart(db, user_id=current_user.id, product_id=item.product_id, quantity=item.quantity)

@router.delete("/{product_id}")
def remove_item_from_cart(product_id: int,
                          db: Session = Depends(get_db),
                          current_user = Depends(get_current_user)):
    success = remove_from_cart(db, user_id=current_user.id, product_id=product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    return {"detail": "Item removed from cart"}

@router.get("/", response_model=list[CartItemResponse])
def view_cart(db: Session = Depends(get_db),
              current_user = Depends(get_current_user)):
    return get_cart_items(db, user_id=current_user.id)
