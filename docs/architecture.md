# Arquitectura del Sistema MVP

Este proyecto utiliza una arquitectura de servicios REST orientada a la validación de datos en tiempo real.

## Diagrama de Flujo de Datos
```mermaid
graph TD
    A[Usuario / Swagger UI] --> B(FastAPI Engine)
    B --> C{Validación Pydantic}
    C -->|Error| E[Respuesta 422]
    C -->|Válido| F{¿Está en Redis?}
    F -->|SÍ| G[Respuesta 200 OK]
    F -->|NO| H[Consulta DB Memoria]
    H --> I[Guardar en Redis]
    I --> G
