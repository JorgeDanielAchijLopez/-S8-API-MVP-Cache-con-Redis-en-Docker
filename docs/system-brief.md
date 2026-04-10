# System Brief – InvControl Pro

## Nombre del sistema

InvControl Pro

---

## Problema que resuelve

Muchos pequeños y medianos negocios gestionan su inventario y ventas de forma manual o mediante herramientas básicas como hojas de cálculo. Esto genera problemas como errores en el registro de productos, inconsistencias en el stock, dificultad para conciliar inventarios y poca visibilidad sobre el estado real del negocio.

Además, la falta de automatización en el control de ventas impide conocer con precisión las ganancias y pérdidas diarias. Estas limitaciones afectan la toma de decisiones y aumentan el riesgo de pérdidas económicas.

InvControl Pro busca resolver estos problemas proporcionando una API que permita gestionar productos, registrar ventas y mantener actualizado el inventario de manera centralizada y automatizada.

---

## Usuarios / Stakeholders

- Dueños de pequeños y medianos negocios
- Personal administrativo
- Desarrolladores que consumen la API
- Evaluador académico (stakeholder indirecto)

---

## Objetivos de éxito

- Permitir el registro y consulta de productos de forma sencilla
- Mantener el stock actualizado automáticamente tras cada venta
- Reducir errores en la gestión de inventario
- Mejorar el tiempo de respuesta en consultas mediante cache

---

## Alcance (Scope)

- Registro de productos
- Consulta de productos por ID
- Registro de ventas
- Actualización de stock
- Implementación de cache con Redis
- API REST accesible mediante HTTP
- Ejecución del sistema mediante Docker Compose

---

## Fuera de alcance (No-scope)

- Autenticación de usuarios
- Interfaz gráfica de usuario (frontend)
- Persistencia en base de datos
- Reportes avanzados financieros
- Integración con sistemas externos

---

## Supuestos

- El sistema será utilizado en un entorno controlado (local o desarrollo)
- El volumen de datos será bajo (MVP)
- Los usuarios tienen conocimientos básicos para interactuar con APIs
- Redis será suficiente como solución de cache

---

## Riesgos y mitigaciones

### 1. Pérdida de datos
Riesgo: los datos se almacenan en memoria y pueden perderse  
Mitigación: en futuras versiones integrar una base de datos persistente

### 2. Datos desactualizados en cache
Riesgo: inconsistencias temporales por uso de TTL  
Mitigación: uso de TTL corto e invalidación de cache en operaciones de escritura

### 3. Dependencia de Redis
Riesgo: falla en el servicio de cache  
Mitigación: fallback a la fuente principal (memoria)

---

## Requerimientos funcionales (FR)

- FR1: El sistema debe permitir crear productos
- FR2: El sistema debe permitir consultar productos por ID
- FR3: El sistema debe permitir registrar ventas
- FR4: El sistema debe actualizar el stock automáticamente
- FR5: El sistema debe permitir actualizar stock manualmente
- FR6: El sistema debe implementar cache en consultas de productos

---

## Requerimientos no funcionales (NFR)

- NFR1: La API debe responder en menos de 2 segundos
- NFR2: El sistema debe poder ejecutarse mediante Docker
- NFR3: El cache debe tener un TTL definido (60 segundos)
- NFR4: El sistema debe ser accesible mediante HTTP REST

---

## Diagrama de contexto

```mermaid
flowchart LR
    User --> API
    API --> Redis
    API --> Memory
