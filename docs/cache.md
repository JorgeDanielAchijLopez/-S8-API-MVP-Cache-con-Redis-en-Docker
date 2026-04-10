# Cache – InvControl Pro

## Endpoint con cache

El endpoint que utiliza cache es:

GET /products/{product_id}

---

## Clave en Redis

Para cada producto se genera una clave con el formato:

product:{product_id}

Ejemplo:

product:1

---

## TTL (Time To Live)

Cada dato almacenado en Redis tiene un tiempo de vida de:

60 segundos

Después de este tiempo, la información se elimina automáticamente.

---

## Estrategia de cache

Se utiliza la estrategia **cache-aside**.

Esto significa que la API es responsable de:

- consultar el cache
- almacenar datos en Redis
- invalidar cache cuando cambia la información

---

## Funcionamiento

### Cache miss

1. El cliente solicita un producto
2. La API busca en Redis
3. No encuentra el dato
4. Consulta la fuente principal (memoria)
5. Guarda el resultado en Redis con TTL
6. Devuelve la respuesta

### Cache hit

1. El cliente solicita un producto
2. La API encuentra el dato en Redis
3. Devuelve la respuesta directamente desde cache

---

## Invalidación de cache

Cuando ocurre una modificación en los datos:

- registro de venta
- actualización de stock

La clave correspondiente en Redis se elimina para evitar datos desactualizados.

---

## Riesgos y limitaciones

- Los datos pueden estar desactualizados durante el tiempo de TTL
- Redis no es persistente en este MVP
- Si el contenedor se reinicia, se pierde el cache
