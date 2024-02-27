from typing import Optional
from app.src.repositories import ProductRepository
from app.src.exceptions import ProductRepositoryException, ProductBusinessException
from .request import DeleteProductRequest
from .response import DeleteProductResponse

class DeleteProduct:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __call__(self, request: DeleteProductRequest) -> Optional[DeleteProductResponse]:
        try:
            self.product_repository.delete(request.product_id)
            return DeleteProductResponse(message="Product deleted successfully.")
        except ProductRepositoryException as e:
            raise ProductBusinessException(str(e))