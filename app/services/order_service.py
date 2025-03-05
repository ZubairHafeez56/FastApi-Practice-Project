from sqlalchemy.orm import Session
from app.models.order_model import Order, OrderItem
from app.models.product_model import Product


def create_order(db: Session, user_id: int, order_items_data: list):
    # order_items_data: list of dicts with product_id and quantity
    order = Order(user_id=user_id, status="delivered")
    db.add(order)
    db.commit()
    db.refresh(order)
    total_amount = 0.0
    for item in order_items_data:
        product = db.query(Product).filter(Product.id == item["product_id"]).first()
        if not product:
            continue
        # For demonstration, assume each product costs 100.0 (or use product.price if available)
        price = 100.0
        order_item = OrderItem(
            order_id=order.id,
            product_id=item["product_id"],
            quantity=item["quantity"],
            price=item["price"] if "price" in item else price,
        )
        total_amount += price * item["quantity"]
        db.add(order_item)
    order.total_amount = total_amount
    db.commit()
    db.refresh(order)
    return order


def get_orders(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()


def get_order_by_id(db: Session, user_id: int, order_id: int):
    return db.query(Order).filter(Order.user_id == user_id, Order.id == order_id).first()
