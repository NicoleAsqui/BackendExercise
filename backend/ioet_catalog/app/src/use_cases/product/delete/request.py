from pydantic import BaseModel

class DeleteProductRequest(BaseModel):
    product_id: str