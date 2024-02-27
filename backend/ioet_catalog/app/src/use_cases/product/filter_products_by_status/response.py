from typing import List
from pydantic import BaseModel

from ....core.models._product import Product

class FilterByStatusResponse(BaseModel):
    products: List[Product]