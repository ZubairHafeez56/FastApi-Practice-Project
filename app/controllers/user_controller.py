from sqlalchemy.orm import Session
from app.models.user_model import User
from app.config.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from app.services.auth_service import register_user, authenticate_user
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse

router = APIRouter()

# Create a DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create or Register User
@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        return register_user(db, user_data)


# User Login
@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user(db, user_data.email, user_data.password)
    if not token:
        return {"error": "Invalid credentials"}
    return {"access_token": token, "token_type": "bearer"}
