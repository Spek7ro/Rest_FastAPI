from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

app = FastAPI()

# app.title = "Mi Primera API"
# app.version = "0.1.0"

# Modelo de datos (Movie) para consultar
class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

# Modelo de datos (MovieCreate) para crear y validar los datos
class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=50)
    overview: str = Field(min_length=10, max_length=100)
    year: int = Field(ge= 1900, le=datetime.datetime.today().year) # le = less or equal (Menor o igual que el año actual)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)

    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 1,
                'title': 'Titanic',
                'overview': 'Una película sobre el famoso barco que se hundió en 1912.',
                'year': 1912,
                'rating': 8.8,
                'category': 'Drama',
            }
        }
    }

# Modelo de datos (MovieUpdate) para actualizar
class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str

# Lista de películas (Lista de objetos de tipo Movie)
movies: List[Movie] = []

# Hola mundo con fast api
@app.get("/", tags=['Home']) 
async def home():
    return "Hola mundo con fast api"

# Podemos crear un endpoint que retorne un diccionario
@app.get("/movies", tags=['Movies'])
async def get_movies() -> List[Movie]:
    return [movie.model_dump() for movie in movies]

# Parametros de ruta
@app.get("/movies/{id}", tags=['Movies'])
async def get_movie_id(id: int) -> Movie:
    movie = next(filter(lambda movie: movie["id"] == id, movies), None)
    if movie:
        return movie.model_dump()
    else:
        return {"error": "Movie not found"}

# Parámetros de query
@app.get("/movies/", tags=['Movies'])
async def get_movie_by_category(category: str) -> Movie:
    movies_by_category = list(filter(lambda movie: movie["category"] == category, movies))
    return movies_by_category.model_dump()

# Método POST (Request Body)
@app.post("/movies", tags=['Movies'])
async def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie) 
    return [movie.model_dump() for movie in movies]

# Método PUT (Actualizar por id)
@app.put("/movies/{id}", tags=['Movies'])
async def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    movie_to_update = next(filter(lambda movie: movie["id"] == id, movies), None)
    if movie_to_update:
        movie_to_update["title"] = movie.title
        movie_to_update["overview"] = movie.overview
        movie_to_update["year"] = movie.year
        movie_to_update["rating"] = movie.rating
        movie_to_update["category"] = movie.category
        return [movie.model_dump() for movie in movies]
    else:
        return {"error": "Movie not found"}

# Método DELETE (Eliminar por id)
@app.delete("/movies/{id}", tags=['Movies'])
async def delete_movie(id: int) -> List[Movie]:
    movie = next(filter(lambda movie: movie["id"] == id, movies), None)
    if movie:
        movies.remove(movie)
        return [movie.model_dump() for movie in movies]
    else:
        return {"error": "Movie not found"}
    