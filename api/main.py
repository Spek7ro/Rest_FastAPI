from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse

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
    return PlainTextResponse("Hola mundo con fast api") # Retorna texto plano

# Podemos crear un endpoint que retorne un diccionario
@app.get("/movies", tags=['Movies'])
async def get_movies() -> List[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)

# Parametros de ruta
@app.get("/movies/{id}", tags=['Movies'])
async def get_movie_id(id: int = Path(gt=0)) -> Movie | dict:
    movie = next(filter(lambda movie: movie.id == id, movies), None)
    if movie:
        return JSONResponse(content=movie.model_dump(), status_code=200)
    else:
        return JSONResponse(content={"error": "Movie not found"}, status_code=404)

# Parámetros de query
@app.get("/movies/", tags=['Movies'])
async def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:
    movies_by_category = next(filter(lambda movie: movie.category == category, movies), None)
    if movies_by_category:
        # return movies_by_category
        return JSONResponse(content=movies_by_category.model_dump(), status_code=200)
    else:
        return JSONResponse(content={"error": "Movie not found"}, status_code=404)

# Método POST (Request Body)
@app.post("/movies", tags=['Movies'])
async def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie) 
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=201)
    # return RedirectResponse('/movies', status_code=302) # Redirección a la ruta /movies codigo 302

# Método PUT (Actualizar por id)
@app.put("/movies/{id}", tags=['Movies'], response_model=Movie)
async def update_movie(movie: MovieUpdate, id: int = Path(gt=0)):
    movie_to_update = next(filter(lambda movie: movie.id == id, movies), None)
    if movie_to_update:
        movie_to_update.title = movie.title
        movie_to_update.overview = movie.overview
        movie_to_update.year = movie.year
        movie_to_update.rating = movie.rating
        movie_to_update.category = movie.category
        return JSONResponse(content=movie_to_update.model_dump(), status_code=200)
    else:
        return JSONResponse(content={"error": "Movie not found"}, status_code=404)

# Método DELETE (Eliminar por id)
@app.delete("/movies/{id}", tags=['Movies'], response_model=Movie)
async def delete_movie(id: int = Path(gt=0)):
    movie_deleted = next(filter(lambda movie: movie.id == id, movies), None)
    if movie_deleted:
        movies.remove(movie_deleted)
        return JSONResponse(content=movie_deleted.model_dump(), status_code=200)
    else:
        return JSONResponse(content={"error": "Movie not found"}, status_code=404)

# Endpoint para retornar un archivo TXT
@app.get("/file", tags=['Files'])
async def get_file():
    return FileResponse('../requirements.txt') 
