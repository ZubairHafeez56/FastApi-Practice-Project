from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItemSchema(BaseModel):
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    order_items: List[OrderItemSchema]

class OrderResponse(BaseModel):
    id: int
    status: str
    total_amount: float
    created_at: datetime
    order_items: List[OrderItemSchema]

    class Config:
        orm_mode = True
