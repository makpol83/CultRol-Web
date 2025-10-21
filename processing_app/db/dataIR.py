import typing
from db import connection

from psycopg import sql

# Parameters:
# conn --> Database connection
# table_data = [table_name, column1_name, column2_name, column3_name, column4_name, ... , columnN_name]
# register_data = [column1_data, column2_data, ... , columnN_data]
# 
def db_insert_register_on_table(conn, table_data : list, register_data : list):
    length = len(table_data)
    length_data = len(register_data)
    if(length < 2 or length -1 - length_data != 0):
        raise Exception

    table_name = table_data[0]
    columns = table_data[1:]  # All columns
    placeholders = ", ".join(["%s"] * length_data)  # %s for each value

    # Make the query secure to any kind of value
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders});"

    with conn.cursor() as cur:
        cur.execute(query, register_data)
    conn.commit()

# PK is a dict with the Primary Keys of the register to delete

def db_clear_register_on_table_on_cascade(conn, table_name, PK: dict):
    where_clause = sql.SQL(" AND ").join(
        sql.Composed([sql.Identifier(col), sql.SQL(" = "), sql.Placeholder(col)])
        for col in PK.keys()
    )

    query = sql.SQL("DELETE FROM {} WHERE {};").format(
        sql.Identifier(table_name),
        where_clause
    )

    with conn.cursor() as cur:
        cur.execute(query, PK) 
    conn.commit()

def db_clear_table_on_cascade(conn, table_name):
    query = sql.SQL("TRUNCATE TABLE {} CASCADE;").format(
        sql.Identifier(table_name)
    )

    with conn.cursor() as cur:
        cur.execute(query)
    conn.commit()

# debug functions
#conn = create_connection()
#db_insert_register_on_table(conn, ['don', 'name', 'EE_use', 'description'], ['DON_TEST', '15', 'DESCR_TEST'])
#db_clear_register_on_table_on_cascade(conn, 'don', {"id_d": 5})
#db_clear_table_on_cascade(conn, 'don')
#close_connection(conn)