import sqlite3
import model


def create_connection():
    connection=sqlite3.connect('Movies.db')
    return connection

def create_table():
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute("""
    Create table if not exists movies (
    id integer primary key autoincrement,
    title text not null,
    director text not null
    
    
    
    )
    """
    )
    connection.commit()
    connection.close()

create_table()

def create_movie(movie: model.MovieCreate):
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute("Insert info movies (title,director) VALUES (?,?)", __parameters=(movie.title,movie.director))
    connection.commit()
    movie_id=cursor.lastrowid
    connection.close()
    return movie_id

def read_movies():
    connection= create_connection()
    connection.row_factory = sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("Select * from movies")
    rows=cursor.fetchall()
    movies=[model.Movie(id=row['id'] , title=row['title'], director=row['director'])for row in rows]
    connection.close()
    return movies

def read_movie(movie_id: int):
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute('Select * from movies where id=?',(movie_id))
    row=cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return model.Movie(id=row['id'] , title=row['title'], director=row['director'])

def update_movie(movie_id: int,movie:model.MovieCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('Update movies set title=?, director=? where id=?', (movie.title,movie.director,movie_id))
    connection.commit()
    updated=cursor.rowcount
    connection.close()
    return updated>0
def delete_movie(movie_id:int):
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute('Delete from movies where id=?', (movie_id))
    connection.commit()
    deleted=cursor.rowcount
    connection.close()
    return deleted>0


