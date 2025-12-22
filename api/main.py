from fastapi import FastAPI, Body
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
    },
    {
        "id": 2,
        "title": "Captain Marvel",
        "overview": "Captain Marvel es un filme de acción dirigido por Chris McKenna y producido por Marvel Studios. El filme se centra en el personaje de Captain America, un agente secreto de la organización S.H.I.E.L.D. que se encuentra en una batalla con el malvado Skrull, Loki, en el espacio de Nueva York.",
        "year": 2019,
        "rating": 9.0,
        "category": "Action"
    },
]


# Hola mundo con fast api
@app.get("/", tags=['Home']) 
async def home():
    return "Hola mundo con fast api"

# Podemos crear un endpoint que retorne un diccionario
@app.get("/movies", tags=['Movies'])
async def get_movies():
    return movies


# Parametros de ruta
@app.get("/movies/{id}", tags=['Movies'])
async def get_movie_id(id: int):
    movie = next(filter(lambda movie: movie["id"] == id, movies), None)
    if movie:
        return movie
    else:
        return {"error": "Movie not found"}


# Parámetros de query
@app.get("/movies/", tags=['Movies'])
async def get_movie_by_category(category: str):
    movies_by_category = list(filter(lambda movie: movie["category"] == category, movies))
    return movies_by_category

# Método POST (Request Body)
@app.post("/movies", tags=['Movies'])
async def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), 
                       year: int = Body(), rating: float = Body(), category: str = Body()):
    new_movie = {
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    }
    movies.append(new_movie)
    return new_movie


# Devolver un html
# @app.get("/movies2", tags=['Home'])
# async def root():
#     return HTMLResponse("<h1>Hola mundo con fast api</h1>"
#                         "<h3>Textoooooooo</h3>"
#                         )

@app.get("/url", tags=['Url']) 
async def url():
    return {"url": "https://fastapi.tiangolo.com/"}


