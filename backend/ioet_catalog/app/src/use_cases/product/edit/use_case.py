from typing import Optional
from app.src.repositories import ProductRepository
from app.src.exceptions import ProductRepositoryException, ProductBusinessException
from .request import EditProductRequest
from .response import EditProductResponse

from app.src.core.models import Product

class EditProduct:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __call__(self, product_id: str, request: EditProductRequest) -> Optional[EditProductResponse]:
        try:
            product = self.product_repository.get_by_id(product_id)
            if not product:
                return None
            
            edited_product = Product(
                product_id=product_id,
                user_id=request.user_id if request.user_id else product.user_id,
                name=request.name if request.name else product.name,
                description=request.description if request.description else product.description,
                price=request.price if request.price else product.price,
                location=request.location if request.location else product.location,
                status=request.status if request.status else product.status,
                is_available=request.is_available if request.is_available else product.is_available
            )

            edited_product = self.product_repository.edit(edited_product)

            edited_product_dict = {
                "product_id": edited_product.product_id,
                "user_id": edited_product.user_id,
                "name": edited_product.name,
                "description": edited_product.description,
                "price": edited_product.price,
                "location": edited_product.location,
                "status": edited_product.status,
                "is_available": edited_product.is_available
            }

            return EditProductResponse(**edited_product_dict)
        except ProductRepositoryException as e:
            raise ProductBusinessException(str(e))