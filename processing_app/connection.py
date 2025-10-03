import psycopg2

# create_connection()
# Creates a connection to a database and returns conn if it was succesful or None if failed 
def create_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="cultrol",
            user="admin",
            password="Gu1!eg1eP81"
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