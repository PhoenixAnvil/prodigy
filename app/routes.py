from fastapi import APIRouter, HTTPException

from app.data import products
from app.models import Product

router = APIRouter()


@router.get("/products", response_model=list[Product])
def list_products():
    return products


@router.post("/products", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product


@router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    for product in products:
        if str(product.id) == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/products/{product_id}")
def delete_product(product_id: str):
    for index, product in enumerate(products):
        if str(product.id) == product_id:
            del products[index]
            return {"detail": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
