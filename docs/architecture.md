graph TD
    A[Usuario / Swagger UI] --> B(FastAPI Engine)
    B --> C{Validación Pydantic}
    C -->|Error| E[Respuesta 422]
    C -->|Válido| F{¿Está en Redis?}
    F -->|SÍ| G[Respuesta 200 OK]
    F -->|NO| H[Consulta DB Memoria]
    H --> I[Guardar en Redis]
    I --> G
    
    style F fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#bbf,stroke:#333,stroke-style:dashed
