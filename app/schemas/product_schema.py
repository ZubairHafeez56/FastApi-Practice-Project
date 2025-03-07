from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True
