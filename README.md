# Project Backend
## Features Added
This project introduces the following features:

Create endpoint to filter a product
Create endpoint to edit a product
Create endpoint to delete a product

## Architecture
The project follows a structured architecture to ensure maintainability, scalability, and clarity in the codebase. It adheres to the following principles:

## Separation of Concerns: 
The project is divided into modules based on their functionalities, such as routes, use cases, repositories, exceptions, and data transfer objects (DTOs).
## Dependency Injection: 
Dependencies are managed using dependency injection, allowing for easier testing, decoupling, and reusability.
## Single Responsibility Principle (SRP): 
Each module is responsible for a single aspect of the application, promoting code that is easier to understand and maintain.

# Implementation Details
## Filtering a Product
Endpoint: GET /products/filter/by_status

This endpoint filters products based on their status.

It leverages the FilterProductsByStatus use case to handle the business logic.

Request DTO: FilterByStatusRequest

Response DTO: FilterByStatusResponse

Sample Postman Data:
![image](https://github.com/NicoleAsqui/BackendExercise/assets/56647127/fabef8de-686e-4733-b08a-c7a72229b6cf)


## Editing a Product
Endpoint: PUT /products/{product_id}

This endpoint allows for editing an existing product.

It utilizes the EditProduct use case to handle the edit operation.

Request DTO: EditProductRequestDto

Response DTO: EditProductResponseDto

Sample Postman Data:
![image](https://github.com/NicoleAsqui/BackendExercise/assets/56647127/59cc89a4-ed2c-42e5-9c70-57e158461a27)


## Deleting a Product
Endpoint: DELETE /products/{product_id}

This endpoint deletes a product based on its ID.

It employs the DeleteProduct use case to manage the deletion process.

Request DTO: DeleteProductRequest

Response DTO: DeleteProductResponseDto

Sample Postman Data:
![image](https://github.com/NicoleAsqui/BackendExercise/assets/56647127/e586171d-40ee-4f7b-9a4f-8e3db0dbc66a)

