# Architecture – InvControl Pro

## Descripción general

La arquitectura del sistema sigue un enfoque simple de tipo API REST orientado a un MVP. Está compuesta por una API desarrollada en FastAPI, un sistema de almacenamiento en memoria para la lógica principal y Redis como capa de cache.

El sistema se ejecuta en contenedores utilizando Docker Compose, lo que permite levantar todos los servicios necesarios con un solo comando.

---

## Componentes principales

### 1. Cliente
Puede ser cualquier consumidor HTTP (navegador, Postman, Swagger UI). Se encarga de enviar solicitudes a la API.

### 2. API (FastAPI)
Contiene la lógica de negocio del sistema:

- Gestión de productos
- Registro de ventas
- Actualización de stock
- Integración con Redis para cache

### 3. Redis (Cache)
Se utiliza como sistema de cache para optimizar consultas frecuentes.

Responsabilidades:

- Almacenar temporalmente datos de productos
- Reducir tiempo de respuesta
- Disminuir carga en la lógica principal

### 4. Almacenamiento en memoria
Estructura interna de la API donde se guardan los datos de productos durante la ejecución del sistema.

---

## Flujo de datos

1. El cliente realiza una solicitud a la API
2. La API verifica si la información existe en Redis
3. Si existe (cache hit), se responde desde Redis
4. Si no existe (cache miss), se obtiene desde memoria
5. La API guarda el resultado en Redis con TTL
6. Se responde al cliente

---

## Diagrama de arquitectura

```mermaid
flowchart LR
    Client --> API
    API --> Redis
    API --> Memory
