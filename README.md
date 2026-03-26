# MVP Sistema de Gestión de Órdenes - UMG

Este es un Producto Mínimo Viable (MVP) desarrollado para el curso de Ingeniería. El sistema permite la gestión de pedidos mediante una API REST funcional.

## Tecnologías utilizadas
* **Lenguaje:** Python 3.14
* **Framework:** FastAPI
* **Validación:** Pydantic Models
* **Documentación:** Swagger UI (OpenAPI 3.1)

## Estructura del Proyecto
* `main.py`: Código fuente de la API con 4 endpoints.
* `docs/api/openapi.json`: Contrato técnico del sistema.
* `docs/architecture.md`: Diagrama de flujo del sistema.

## Cómo ejecutar
1. Instalar dependencias: `pip install fastapi uvicorn`
2. Correr servidor: `uvicorn main:app --reload`
3. Ver documentación: http://127.0.0.1:8000/docs
