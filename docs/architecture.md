# Architecture – InvControl Pro

## Descripción general

El sistema sigue una arquitectura simple basada en API REST.

Está compuesto por:

- API (FastAPI)
- Redis (cache)
- Almacenamiento en memoria

---

## Componentes

### API (FastAPI)

Responsable de:

- Exponer endpoints
- Validar datos
- Gestionar lógica de negocio
- Integrarse con Redis

---

### Redis

Responsable de:

- Almacenar datos en cache
- Reducir tiempos de respuesta
- Disminuir carga en la lógica principal

---

### Memoria (diccionarios)

Responsable de:

- Almacenar datos temporalmente
- Servir como fuente principal de datos

---

## Diagrama de arquitectura

```mermaid
flowchart LR
    Client --> API
    API --> Redis
    API --> Memory

    Redis --> API
    Memory --> API
