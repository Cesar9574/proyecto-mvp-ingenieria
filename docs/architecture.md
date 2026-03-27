# Arquitectura del Sistema MVP

Este proyecto utiliza una arquitectura de servicios REST orientada a la validación de datos en tiempo real.

## Diagrama de Flujo de Datos
```mermaid
graph TD
    A[Usuario / Swagger UI] -->|Petición JSON| B(FastAPI Engine)
    B --> C{Validación Pydantic}
    C -->|Datos Válidos| D[Base de Datos en Memoria]
    C -->|Error de Validación| E[Respuesta 422 Unprocessable Entity]
    D --> F[Respuesta 201 Created / 200 OK]