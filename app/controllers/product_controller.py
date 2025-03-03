from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.utils.security import get_current_user

router = APIRouter()

# Database Connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Allow only authenticated users to create products."""
    new_product = Product(**product.dict(), user_id=current_user.id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=list[ProductResponse])
def get_own_products(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Fetch only the logged-in user's products."""
    return db.query(Product).filter(Product.user_id == current_user.id).all()

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_data: ProductCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Allow only the owner to update the product."""
    product = db.query(Product).filter(Product.id == product_id, Product.user_id == current_user.id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product_data.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Allow only the owner to delete the product."""
    product = db.query(Product).filter(Product.id == product_id, Product.user_id == current_user.id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
