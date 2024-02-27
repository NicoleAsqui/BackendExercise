from pydantic import BaseModel

class DeleteProductResponse(BaseModel):
    message: str