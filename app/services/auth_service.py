from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.utils.security import hash_password, verify_password, create_access_token
from app.schemas.user_schema import UserCreate
from datetime import timedelta

def register_user(db: Session, user_data: UserCreate):
    hashed_password = hash_password(user_data.password)
    new_user = User(username=user_data.username, email=user_data.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, email: EmailStr, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    return create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=30))
