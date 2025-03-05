from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.order_schema import OrderCreate, OrderResponse
from app.services.order_service import create_order, get_orders, get_order_by_id
from app.config.database import SessionLocal
from app.utils.security import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderResponse)
def place_order(order_data: OrderCreate,
                db: Session = Depends(get_db),
                current_user = Depends(get_current_user)):
    # Convert each order item to dict
    items = [item.dict() for item in order_data.order_items]
    order = create_order(db, user_id=current_user.id, order_items_data=items)
    return order

@router.get("/", response_model=list[OrderResponse])
def list_orders(db: Session = Depends(get_db),
                current_user = Depends(get_current_user)):
    return get_orders(db, user_id=current_user.id)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int,
              db: Session = Depends(get_db),
              current_user = Depends(get_current_user)):
    order = get_order_by_id(db, user_id=current_user.id, order_id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
