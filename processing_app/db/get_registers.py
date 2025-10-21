import psycopg
from db import connection
from db import dataIR
from psycopg import sql
from db.enums_dicts import PRIMARY_KEYS

# Returns all the registers from the table name received
# Returns a list of dictionaries where each list is a dictionary with column_name | value
def get_registers_from_table(conn, table_name: str):

    # We configure row_factory to access name per column
    conn.row_factory = psycopg.rows.dict_row
    cur = conn.cursor()
    
    try:

        query = sql.SQL("SELECT * FROM {table};").format(
            table = sql.Identifier(table_name)
        )

        cur.execute(query)
        registros = cur.fetchall()  # Lista de diccionarios
        return registros
    except Exception as e:
        print(f"Error al obtener registros de {table_name}: {e}")
        return []
    finally:
        cur.close()

# Returns the register with the PK received by argument
def get_registers_from_table_with_PK(conn, table_name: str, primary_keys: list):

    # We configure row_factory to access name per column
    conn.row_factory = psycopg.rows.dict_row
    cur = conn.cursor()
    
    try:
        columns = PRIMARY_KEYS[table_name]
        length = len(primary_keys)
        if len(columns) != length:
            raise Exception

        where_clause = sql.SQL(" AND ").join(
            sql.SQL("{} = %s").format(sql.Identifier(col)) for col in columns
        )

        query = sql.SQL("SELECT * FROM {table} WHERE {where};").format(
            table = sql.Identifier(table_name),
            where = where_clause
        )

        cur.execute(query, tuple(primary_keys))
        register = cur.fetchall()  # List of diccionaries
        return register
    except Exception as e:
        print(f"Error when getting registers from {table_name}: {e}")
        return []
    finally:
        cur.close()

# debug functions
#conn = connection.create_connection()
#dataIR.db_insert_register_on_table(conn, ['don', 'name', 'EE_use', 'description'], ['DON_TEST', '15', 'DESCR_TEST'])
#dataIR.db_insert_register_on_table(conn, ['don', 'name', 'EE_use', 'description'], ['DON_TEST', '16', 'DESCR_TEST'])
#lst_all = get_registers_from_table(conn, 'don')
#print(f'{lst_all}')
#lst = get_registers_from_table_with_PK(conn, 'don', ['13'])
#print(f'{lst}')
#dataIR.db_clear_register_on_table_on_cascade(conn, 'don', {"id_d": 5})
#dataIR.db_clear_table_on_cascade(conn, 'don')
#connection.close_connection(conn)