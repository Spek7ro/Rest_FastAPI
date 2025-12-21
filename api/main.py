from fastapi import FastAPI

app = FastAPI()

# Iniciar el servidor uvicorn main:app --reload

# Hola mundo con fast api
@app.get("/") 
async def root():
    return {"Hello": "World",
            "Hola": "Mundo", 
            "Bienvenido": "a FastAPI",
            "Python": "es una mierda"
            }

@app.get("/url") 
async def url():
    return {"url": "https://fastapi.tiangolo.com/"}


