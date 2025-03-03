from fastapi import FastAPI
from app.config.database import Base, engine
from app.routes import user, product

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register Routes
app.include_router(user.router, prefix="/api", tags=["Users"])
app.include_router(product.router, prefix="/api/user", tags=["Products"])

@app.get("/")
def home():
    return {"message": "FastAPI MVC App is running!"}
