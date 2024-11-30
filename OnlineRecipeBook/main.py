from fastapi import FastAPI
from routers import recipe, Category
import os
from dotenv import load_dotenv
from database import get_db_connection
import uvicorn

load_dotenv()

Database_Url=os.getenv("Database_url")
app=FastAPI()
app.include_router(recipe.router)
app.include_router(Category.router)
@app.on_event("startup")
def startup():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists categories (
        id integer primary key autoincrement
        name text unique not null
            
        )
    """)
    cursor.execute("""create table if not exists categories (
        id integer primary key autoincrement,
        name text not null,
        description text,
        ingredients text,
        cuisine text,
        difficulty text,
        category_id integer,
        foreign key(category_id) references categories (id)
    
    
    )
    
    """)
    conn.commit()
    conn.close()

@app.get("/")
def read_root():
    return {"message":"FASTAPI with SQL lite project"}
