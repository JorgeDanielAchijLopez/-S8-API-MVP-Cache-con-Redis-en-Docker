from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import json

app = FastAPI(title="InvControl Pro API")

# Conexión a Redis (usa "redis" porque así se llama el contenedor)
r = redis.Redis(host="redis", port=6379, decode_responses=True)

#  Base de datos en memoria
products = {}

#  Modelo Producto
class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

#  Modelo Venta
class Sale(BaseModel):
    product_id: int
    quantity: int

#  Crear producto
@app.post("/products")
def create_product(product: Product):
    products[product.id] = product
    return {"message": "Producto creado"}

#  Obtener producto (CON CACHE )
@app.get("/products/{product_id}")
def get_product(product_id: int):

    cache_key = f"product:{product_id}"

    # 1. Buscar en Redis
    cached = r.get(cache_key)

    if cached:
        return {
            "source": "cache",
            "data": json.loads(cached)
        }

    # 2. Si no está en memoria
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    product = products[product_id]

    # 3. Guardar en Redis (TTL 60 segundos)
    r.setex(cache_key, 60, json.dumps(product.dict()))

    return {
        "source": "db",
        "data": product
    }

#  Registrar venta
@app.post("/sales")
def create_sale(sale: Sale):

    if sale.product_id not in products:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    product = products[sale.product_id]

    if product.stock < sale.quantity:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    product.stock -= sale.quantity

    # Invalidar cache
    cache_key = f"product:{sale.product_id}"
    r.delete(cache_key)

    return {"message": "Venta registrada"}

#  Actualizar stock
@app.put("/products/{product_id}/stock")
def update_stock(product_id: int, stock: int):

    if product_id not in products:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    products[product_id].stock = stock

    # Invalidar cache
    cache_key = f"product:{product_id}"
    r.delete(cache_key)

    return {"message": "Stock actualizado"}
