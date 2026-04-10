# Requirements – InvControl Pro

## Backlog

Link al tablero (Trello):
https://trello.com/invite/b/69a13d69fc56024f57f95125/ATTIfdd25a428ed3c6fcf224fff46a57acd0C0F953F1/invcontrol-pro-product-backlog 


---

## Historias de usuario

### 1. Crear producto  
**Prioridad:** Must  

Como usuario, quiero registrar un producto para poder gestionarlo en el sistema.

---

### 2. Consultar producto  
**Prioridad:** Must  

Como usuario, quiero consultar un producto por ID para conocer su información.

---

### 3. Registrar venta  
**Prioridad:** Must  

Como usuario, quiero registrar una venta para actualizar el inventario automáticamente.

---

### 4. Actualizar stock  
**Prioridad:** Should  

Como usuario, quiero actualizar manualmente el stock para corregir inconsistencias.

---

### 5. Visualizar estado del inventario  
**Prioridad:** Could  

Como usuario, quiero visualizar el estado del inventario para tener control de los productos.

---

### 6. Implementar cache con Redis  
**Prioridad:** Must  

Como sistema, quiero almacenar en cache las consultas de productos para mejorar el rendimiento.

---

### 7. Invalidar cache al modificar datos  
**Prioridad:** Must  

Como sistema, quiero eliminar el cache cuando cambian los datos para evitar inconsistencias.

---

### 8. Levantar sistema con Docker Compose  
**Prioridad:** Must  

Como desarrollador, quiero ejecutar el sistema con Docker para facilitar el despliegue.

---

### 9. Optimizar consultas usando cache  
**Prioridad:** Must  

Como sistema, quiero responder consultas desde Redis para mejorar el rendimiento.

---

### 10. Medir rendimiento del cache  
**Prioridad:** Should  

Como sistema, quiero comparar respuestas con y sin cache para validar la mejora.

---

## Criterios de aceptación (Given / When / Then)

### Historia 2: Consultar producto

Given que existe un producto registrado  
When el usuario realiza una solicitud GET /products/{id}  
Then el sistema devuelve la información del producto  

Given que el producto no existe  
When el usuario realiza la solicitud  
Then el sistema responde con error 404  

---

### Historia 6: Implementar cache con Redis

Given que el producto no está en cache  
When el usuario consulta el producto  
Then el sistema obtiene los datos y los guarda en Redis con TTL  

Given que el producto ya está en cache  
When el usuario consulta nuevamente  
Then el sistema responde desde Redis  

---

## Estado del backlog

El backlog ha sido actualizado para incluir funcionalidades relacionadas con rendimiento mediante cache.

Las historias críticas (Must) han sido completadas, incluyendo la implementación de Redis y su integración con la API. Algunas tareas se encuentran en progreso, principalmente documentación y pruebas.

El tablero refleja el avance del proyecto con tareas distribuidas en To Do, In Progress y Done.
