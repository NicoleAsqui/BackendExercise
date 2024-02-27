from decimal import Decimal
from app.src.core.enums import ProductStatuses
from pydantic import BaseModel

class EditProductResponse(BaseModel):
    product_id: str
    user_id: str
    name: str
    description: str | None
    price: Decimal
    location: str
    status: ProductStatuses
    is_available: bool