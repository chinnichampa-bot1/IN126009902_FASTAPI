from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "FastAPI is working"}

products = [
    {"id":1,"name":"Wireless Mouse","price":499,"category":"Electronics","in_stock":True},
    {"id":2,"name":"Notebook","price":99,"category":"Stationery","in_stock":True},
    {"id":3,"name":"Pen Set","price":49,"category":"Stationery","in_stock":True},
    {"id":4,"name":"USB Cable","price":199,"category":"Electronics","in_stock":False},
    {"id":5,"name":"Laptop Stand","price":1299,"category":"Electronics","in_stock":True},
    {"id":6,"name":"Mechanical Keyboard","price":2499,"category":"Electronics","in_stock":True},
    {"id":7,"name":"Webcam","price":1899,"category":"Electronics","in_stock":False}
]


# Q2
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }
# Q4
@app.get("/products/category/{category}")
def get_by_category(category: str):
    result = []
    for product in products:
        if product["category"].lower() == category.lower():
            result.append(product)
    return {"products": result}
# Q5
@app.get("/products/in-stock")
def get_in_stock_products():
    in_stock_products = [p for p in products if p["in_stock"]]
    return {
        "products": in_stock_products,
        "total": len(in_stock_products)
    }
# Q3
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

