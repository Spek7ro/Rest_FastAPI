# FastAPI
Curso de creación de api´s usando la tecnología FastAPI 

### Crear entorno virtual
```
python -m venv venv
```

### Activar entorno virtual
```
source venv/bin/activate o .\venv\Scripts\activate (windows)
```

### Instalación de FastAPI y uvicorn
```
pip install fastapi uvicorn
```
### Ejecutar el servidor
```
cd api
uvicorn main:app --reload
```
### Documentación de FastAPI (Swagger y Redoc)
```
localhost:8000/docs

localhost:8000/redoc
```