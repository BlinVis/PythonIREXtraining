import sqlite3
from typing import  List
from streamlit import status
from models.category import CategoryBase, Category
from database import get_db_connection
from fastapi import APIRouter, HTTPException
router=APIRouter()
@router.get('/categories/',List[Category])
def get_categories():
    conn=get_db_connection()
    cursor=conn.cursor()

