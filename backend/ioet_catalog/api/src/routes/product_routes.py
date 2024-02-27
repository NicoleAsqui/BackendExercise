from typing import List
from app.src.exceptions.business.product import ProductBusinessException

from fastapi import APIRouter, Depends, HTTPException

from app.src.use_cases import (
    ListProducts, 
    ListProductResponse, 
    FindProductById, 
    FindProductByIdResponse, 
    FindProductByIdRequest, 
    CreateProduct, 
    CreateProductResponse, 
    CreateProductRequest,
    FilterProductsByStatus,
    FilterByStatusRequest,
    FilterByStatusResponse,
    EditProduct,
    DeleteProduct,
    DeleteProductRequest,

)
from ..dtos import (
    ProductBase,
    ListProductResponseDto, 
    CreateProductRequestDto,
    CreateProductResponseDto,
    FindProductByIdResponseDto,
    EditProductResponseDto,
    EditProductRequestDto,
    DeleteProductResponseDto
)
from factories.use_cases import (
    list_product_use_case, 
    find_product_by_id_use_case,
    create_product_use_case,
    create_product_use_case,
    filter_product_by_status_use_case,
    edit_product_use_case,
    delete_product_use_case
)
from app.src.core.models import Product

product_router = APIRouter(prefix="/products")

@product_router.get("/", response_model=ListProductResponseDto)
async def get_products(
    use_case: ListProducts = Depends(list_product_use_case)
) -> ListProductResponse:
    response = use_case()
    products = [
        ProductBase(**{
            **product._asdict(),
            "status": product.status.value
        }) 
        for product in response.products
    ]
    response_dto: ListProductResponseDto = ListProductResponseDto(products=products)
    return response_dto

@product_router.get("/{product_id}", response_model=FindProductByIdResponseDto)
async def get_product_by_id(
    product_id: str,
    use_case: FindProductById = Depends(find_product_by_id_use_case)
) -> FindProductByIdResponse:
    response = use_case(FindProductByIdRequest(product_id=product_id))
    response_dto: FindProductByIdResponseDto = FindProductByIdResponseDto(**response._asdict())
    return response_dto

@product_router.post("/", response_model=CreateProductResponseDto)
async def create_product(
    request: CreateProductRequestDto,
    use_case: CreateProduct = Depends(create_product_use_case)
) -> CreateProductResponse:
    response = use_case(CreateProductRequest(
        product_id=request.product_id, 
        user_id=request.user_id, 
        name=request.name, 
        description=request.description, 
        price=request.price, 
        location=request.location, 
        status=request.status, 
        is_available=request.is_available
    ))
    response_dto: CreateProductResponseDto = CreateProductResponseDto(**response._asdict())
    return response_dto


@product_router.get("/filter/by_status", response_model=FilterByStatusResponse)
async def filter_products_by_status(
    status: str,
    filter_use_case: FilterProductsByStatus = Depends(filter_product_by_status_use_case),
) -> FilterByStatusResponse:
    request = FilterByStatusRequest(status=status)
    response = filter_use_case(request)
    return response

@product_router.put("/{product_id}", response_model=EditProductResponseDto)
async def edit_product(
    product_id: str,
    request: EditProductRequestDto,
    use_case: EditProduct = Depends(edit_product_use_case)
) -> EditProductResponseDto:
    response = use_case(product_id, EditProductRequestDto(
        user_id=request.user_id,         
        name=request.name, 
        description=request.description, 
        price=request.price, 
        location=request.location, 
        status=request.status, 
        is_available=request.is_available
    ))

    if response:
        response_dto: EditProductResponseDto = EditProductResponseDto(
            product_id=response.product_id,
            user_id=response.user_id,
            name=response.name,
            description=response.description,
            price=response.price,
            location=response.location,
            status=response.status.value,
            is_available=response.is_available
        )
        return response_dto

@product_router.delete("/{product_id}", response_model=DeleteProductResponseDto)
async def delete_product(
    product_id: str,
    use_case: DeleteProduct = Depends(delete_product_use_case)
) -> DeleteProductResponseDto:
    try:
        response = use_case(DeleteProductRequest(product_id=product_id))
        if not response:
            raise HTTPException(status_code=404, detail="Product not found")
        return DeleteProductResponseDto(message="Product deleted successfully.")
    except ProductBusinessException as e:
        raise HTTPException(status_code=400, detail=str(e))