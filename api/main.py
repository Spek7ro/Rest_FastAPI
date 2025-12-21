from fastapi import FastAPI

app = FastAPI()

# app.title = "Mi Primera API"
# app.version = "0.1.0"

# Iniciar el servidor uvicorn main:app --reload

# Hola mundo con fast api
@app.get("/", tags=['Home']) 
async def root():
    return {"Hello": "World",
            "Hola": "Mundo", 
            "Bienvenido": "a FastAPI",
            "Python": "Es un lenguaje de programación",
            }

@app.get("/url", tags=['Url']) 
async def url():
    return {"url": "https://fastapi.tiangolo.com/"}


