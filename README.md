# Transitrack API

## Descripción

API REST para gestionar conductores y rutas de transporte. Permite crear, listar, actualizar y eliminar conductores y rutas, así como asociar cada ruta con un conductor. También incluye funcionalidad de búsqueda por origen, destino u horario de las rutas.

---

## Tecnologías usadas

- Python 3.12  
- Django 5.2  
- Django REST Framework  
- drf-yasg (Swagger UI para documentación)  
- SQLite (base de datos por defecto)

---

## Instrucciones para ejecutar el servidor

##### 1. Clonar el repositorio y entrar al directorio del proyecto:

   ```bash
   git clone <url-del-repositorio>
   cd transitrack_api_project
   ```
##### 2. Crear y activar entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

##### 3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

##### 4. Aplicar migraciones:
```bash
python manage.py migrate
```

##### 5. Ejecutar el servidor:
```bash
python manage.py runserver
```

##### 6. Acceder a la documentación Swagger (opcional):
```bash
http://127.0.0.1:8000/swagger/
```

## Endpoints disponibles con ejemplos
# Conductores

##### Listar conductores
```bash
curl -X GET http://127.0.0.1:8000/api/conductores/
```
##### Crear conductor
```bash
curl -X POST http://127.0.0.1:8000/api/conductores/ -H "Content-Type: application/json" -d '{"nombre": "Luis Martínez", "numero_licencia": "LMN456"}'
```

##### Leer conductor (ID=3)
```bash
curl -X GET http://127.0.0.1:8000/api/conductores/3/
```

##### Actualizar conductor (ID=3)
```bash
curl -X PATCH http://127.0.0.1:8000/api/conductores/3/ -H "Content-Type: application/json" -d '{"numero_licencia": "LMN888"}'
```

##### Eliminar conductor (ID=3)
```bash
curl -X DELETE http://127.0.0.1:8000/api/conductores/3/
```
## Rutas

##### Listar rutas
```bash
curl -X GET http://127.0.0.1:8000/api/rutas/
```

##### Crear ruta
```bash
curl -X POST http://127.0.0.1:8000/api/rutas/ -H "Content-Type: application/json" -d '{"origen": "Ciudad A", "destino": "Ciudad B", "horario": "10:00 AM", "conductor_id": 3}'
```

##### Leer ruta (ID=3)
```bash
curl -X GET http://127.0.0.1:8000/api/rutas/3/
```

##### Actualizar ruta (ID=3)
```bash
curl -X PATCH http://127.0.0.1:8000/api/rutas/3/ -H "Content-Type: application/json" -d '{"destino": "Ciudad C"}'
```

##### Eliminar ruta (ID=3)
```bash
curl -X DELETE http://127.0.0.1:8000/api/rutas/3/
```

##### Buscar rutas con filtro

Buscar rutas cuyo origen, destino o horario contengan el texto "Ciudad":
```bash
curl -X GET "http://127.0.0.1:8000/api/rutas/?search=Ciudad"
```

#### Video demostrativo del funcionamiento de mi proyecto: 
- Link: https://youtu.be/7ubC9WJnRkc 
#### Autora: Ailyn Medina
