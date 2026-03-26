from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="MVP Sistema de Órdenes - UMG")

# Modelo con validación (Cumple Requisito D: Pydantic)
class Order(BaseModel):
    id: int
    customer: str = Field(..., min_length=3, description="Nombre del cliente")
    amount: float = Field(..., gt=0, description="Monto mayor a 0")
    status: str = "Pending"

# Base de datos en memoria (Simulada)
db = []

# 1. Crear Orden (POST) - Operación de creación
@app.post("/orders", status_code=201)
async def create_order(order: Order):
    if any(o.id == order.id for o in db):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    db.append(order)
    return order

# 2. Consultar por ID (GET) - Operación de consulta
@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    order = next((o for o in db if o.id == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return order

# 3. Listar todas (GET) - Endpoint adicional
@app.get("/orders")
async def list_orders():
    return db

# 4. Actualizar Estado (PATCH) - Cambio de estado
@app.patch("/orders/{order_id}/status")
async def update_status(order_id: int, status: str):
    order = next((o for o in db if o.id == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="No se encontró la orden")
    order.status = status
    return order
