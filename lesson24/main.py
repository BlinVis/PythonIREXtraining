from http.client import HTTPException

from fastapi import FastAPI
import model
import database


app=FastAPI()

@app.get('/')
def read_root():
    return {'message':' welcome to the movies crud api'}

@app.post("/movies/", response_model=model.Movie)
def create_movie(movie: model.MovieCreate):
    movie_id=database.create_movie(movie)
    return model.Movie(id=movie_id,**movie.dict())

@app.get('/movies/',response_model=list[model.Movie])
def read_movies():
    return database.read_movies()
@app.get('/movies/', response_model=model.Movie)
def read_movie(movie_id=int):
    movie=database.read_movies(movie_id)
    if movie is None:
        raise  HTTPException(status_code=404,details='movie not found')
    return movie
@app.put('/movies/{movie_id}', response_model=model.Movie)
def update_movie(movie_id: int, movie:model.MovieCreate):
    updated=database.update_movie(movie_id,movie)
    if not updated:
        raise HTTPException(status_code=404,details='movie not found')
    return model.Movie(id=movie_id, **movie.dict())
@app.delete('/movies/{movie_id}',response_model=dict)
def delete_movie(movie_id=int):
    deleted=database.delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404, details='movie not found')
    return {'message':'Movie deleted'}





