import psycopg

from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# create_connection()
# Creates a connection to a database and returns conn if it was succesful or None if failed 
def create_connection():
    try:
        conn = psycopg.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connection established")
        return conn
    except Exception as e:
        print("Error when connecting:", e)
        return None
    
# close_connection()
# Closes a connection to the database.
def close_connection(conn):
    if conn is not None:
        conn.close()
        conn = None
        print("Connection closed")