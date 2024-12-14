import sqlite3
from typing import List
from fastapi import APIRouter,HTTPException,status,Depends
from finalproject.models.book import Book,BookCreate
from auth.security import get_api_key
from finalproject.database import get_db_connection

router=APIRouter()

@router.get("/",response_model=List[Book])
def get_books():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("select from id,title,author_id,book_link,genres,average_rating,published_year from books")
    books=cursor.fetchall()

    conn.close()

    return [{
        "id":book[0],
        "title": book[1],
        "author_id": book[2],
        "book_link": book[3],
        "genres": book[4].split(",") if book[4] else [],

        "average_rating": book[5],
        "published_year": book[6]
    } for book in books]
@router.post("/",response_model=Book)
def create_book(book:BookCreate,_:str=Depends(get_api_key)):
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        genres=",".join(book.genres)
        cursor.execute("insert into books(title,author_id,book_link,genres,average_rating,published_year)"
                       "values(?,?,?,?,?,?)",(book.title,book.author_id,book.book_link,genres,book.average_rating,book.published_year))
        conn.commit()
        book_id=cursor.lastrowid
        return Book(id=book_id,**book.dict())
    except sqlite3.InternalError:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,

            detail=f"Book{book.title} already exists"
        )
    finally:
        conn.close()
@router.put("/{book_id}",response_model=Book)
def update_book(book_id:int,book:BookCreate,_:str=Depends(get_api_key)):
    conn=get_db_connection()
    cursor=conn.cursor()
    genres=", ".join(book.genres)
    cursor.execute("Update books set title=?, author_id=?,book_link=?,genres=?,average_rating=?,published_year=? where id=?",(
        book.title,book.author_id,book.book_link,genres,book.average_rating,book.published_year,book_id
    ))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    conn.commit()
    conn.close()
    return Book(id=book_id, **book.dict())

@router.delete("/{book_id}",response_model=dict)
def delete_book(bookd_id:int,_:str=Depends(get_api_key)):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("Delete from books where id=?",(bookd_id))
    if cursor.rowcount==0:
        conn.close()
        raise HTTPException(status_code=404,detail="Book not found")
    conn.commit()
    conn.close()
    return {"Detail":"Book deleted"}






