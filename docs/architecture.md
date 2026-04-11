graph TD
    A[Usuario / Swagger UI] -->|Petición JSON| B(FastAPI Engine)
    B --> C{Validación Pydantic}
    
    C -->|Error de Validación| E[Respuesta 422 Unprocessable Entity]
    
    C -->|Datos Válidos| F{¿Está en Redis?}
    
    F -->|SÍ: Cache Hit| G[Respuesta 200 OK]
    
    F -->|NO: Cache Miss| H[Consulta Lista/DB Memoria]
    H --> I[Guardar en Redis - TTL 60s]
    I --> G
    
    style F fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#bbf,stroke:#333,stroke-style:dashed
