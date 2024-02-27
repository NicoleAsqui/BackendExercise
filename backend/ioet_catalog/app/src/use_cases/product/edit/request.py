from decimal import Decimal
from typing import Optional
from app.src.core.enums import ProductStatuses

class EditProductRequest:
    def __init__(
        self,
        user_id: str,
        name: str,
        description: Optional[str],
        price: Decimal,
        location: str,
        status: ProductStatuses,
        is_available: bool
    ) -> None:
        self.user_id = user_id
        self.name = name
        self.description = description
        self.price = price
        self.location = location
        self.status = status
        self.is_available = is_available