from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import redis
import json
import os

app = FastAPI(title="MVP Sistema de Órdenes con Cache - UMG")

# Configuración de Redis
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
cache = redis.from_url(REDIS_URL)

class Order(BaseModel):
    id: int
    customer: str = Field(..., min_length=3)
    amount: float = Field(..., gt=0)
    status: str = "Pending"

# Base de datos simulada en memoria
db = []

@app.post("/orders", status_code=201)
async def create_order(order: Order):
    if any(o.id == order.id for o in db):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    db.append(order)
    return order

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    cache_key = f"order_id:{order_id}"
    
    # Intentar obtener de Redis
    order_cacheada = cache.get(cache_key)
    
    if order_cacheada:
        print(f"--- CACHE HIT (ID: {order_id} recuperado de Redis) ---")
        return json.loads(order_cacheada)

    # Si no está en cache, buscar en la "DB"
    print(f"--- CACHE MISS (ID: {order_id} buscando en base de datos) ---")
    order = next((o for o in db if o.id == order_id), None)
    
    if not order:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    
    # Guardar en Redis por 60 segundos
    cache.setex(cache_key, 60, json.dumps(order.dict()))
    
    return order

@app.get("/orders")
async def list_orders():
    return db

@app.patch("/orders/{order_id}/status")
async def update_status(order_id: int, status: str):
    order = next((o for o in db if o.id == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="No se encontró la orden")
    
    order.status = status
    # Importante: Borrar el cache si el dato cambia
    cache.delete(f"order_id:{order_id}")
    print(f"--- CACHE DELETED (Se actualizó el estado de la orden {order_id}) ---")
    return order