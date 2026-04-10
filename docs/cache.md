# Cache – InvControl Pro

## Endpoint(s) que usan cache

El endpoint que utiliza cache es:

GET /products/{product_id}

Este endpoint fue seleccionado porque es una operación de lectura frecuente.

---

## Claves de Redis

Las claves generadas en Redis siguen el siguiente formato:

product:{product_id}

Ejemplo:

product:1

---

## TTL definido

Se definió un TTL (Time To Live) de:

60 segundos

Esto permite que los datos se mantengan actualizados y evita inconsistencias prolongadas.

---

## Estrategia de cache

Se utiliza la estrategia:

Cache-Aside

Flujo:

1. La API recibe la solicitud
2. Busca en Redis
3. Si existe → responde desde cache
4. Si no existe → obtiene datos desde memoria
5. Guarda en Redis con TTL
6. Responde al cliente

---

## Comportamiento del sistema

### Cache Hit

Cuando el dato ya está en Redis:

- Se responde directamente desde cache
- No se consulta la fuente principal
- Mejora el tiempo de respuesta

---

### Cache Miss

Cuando el dato no está en Redis:

- Se consulta la fuente principal (memoria)
- Se guarda en Redis
- Se devuelve la respuesta

---

## Invalidación de cache

Cuando se actualiza el stock o se registra una venta:

- Se elimina la clave correspondiente en Redis
- Esto evita devolver datos desactualizados

---

## Riesgos y limitaciones

### 1. Datos desactualizados
Puede haber inconsistencias durante el TTL

### 2. Dependencia de Redis
Si Redis falla, el sistema pierde el beneficio del cache

### 3. Almacenamiento en memoria
Los datos principales no son persistentes

### 4. TTL fijo
No se adapta dinámicamente a cambios del sistema
