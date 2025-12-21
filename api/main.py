from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# app.title = "Mi Primera API"
# app.version = "0.1.0"

movies = [
    {
        "id": 1,
        "title": "Avengers: Endgame",
        "overview": "Avengers: Endgame es un filme de acción dirigido por Joss Whedon y producido por Marvel Studios. El filme se centra en los personajes de Ant-Man y Vision, dos agentes secretos de la organización S.H.I.E.L.D. que se encuentran en una batalla con el malvado Skrull, Loki, en el espacio de Nueva York.",
        "year": 2019,
        "rating": 8.8,
        "category": "Action"
    }
]


# Hola mundo con fast api
@app.get("/", tags=['Home']) 
async def root():
    return "Hola mundo con fast api"

# Podemos crear un endpoint que retorne un diccionario
@app.get("/movies", tags=['Home'])
async def get_movies():
    return movies


# Parametros de ruta
@app.get("/movies/{id}", tags=['Home'])
async def get_movie_id(id: int):
    movie = next(filter(lambda movie: movie["id"] == id, movies), None)
    if movie:
        return movie
    else:
        return {"error": "Movie not found"}


# Devolver un html
# @app.get("/movies2", tags=['Home'])
# async def root():
#     return HTMLResponse("<h1>Hola mundo con fast api</h1>"
#                         "<h3>Textoooooooo</h3>"
#                         )

@app.get("/url", tags=['Url']) 
async def url():
    return {"url": "https://fastapi.tiangolo.com/"}


