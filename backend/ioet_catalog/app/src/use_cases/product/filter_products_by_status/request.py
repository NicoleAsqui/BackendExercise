from pydantic import BaseModel
from app.src.core.enums import ProductStatuses

class FilterByStatusRequest(BaseModel):
    status: ProductStatuses