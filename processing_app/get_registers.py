import psycopg
import connection
import data_insertion_removal
from enums_dicts import PRIMARY_KEYS

# Returns all the registers from the table name received
# Returns a list of dictionaries where each list is a dictionary with column_name | value
def get_registers_from_table(conn, table_name: str):

    # We configure row_factory to access name per column
    conn.row_factory = psycopg.rows.dict_row
    cur = conn.cursor()
    
    try:
        query = f'SELECT * FROM "{table_name}";'
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
        query = f'SELECT * FROM "{table_name} " WHERE '
        lst = PRIMARY_KEYS[table_name]
        length = len(primary_keys)
        if lst != length:
            raise Exception
        if length == 1:
            query += lst[0] + " = " + primary_keys[0] + ";"
        else:
            query += "("
            for i in range(length - 1):
                query += lst[i] + ", "
            query += lst[length - 1] + ") = "

            query += "("
            for i in range(length - 1):
                query += primary_keys[i] + ", "
            query += primary_keys[length - 1] + ");"

        cur.execute(query)
        registros = cur.fetchall()  # Lista de diccionarios
        return registros
    except Exception as e:
        print(f"Error al obtener registros de {table_name}: {e}")
        return []
    finally:
        cur.close()

# debug functions
conn = connection.create_connection()
data_insertion_removal.db_insert_register_on_table(conn, ['don', 'name', 'EE_use', 'description'], ['DON_TEST', '15', 'DESCR_TEST'])
data_insertion_removal.db_insert_register_on_table(conn, ['don', 'name', 'EE_use', 'description'], ['DON_TEST', '16', 'DESCR_TEST'])
lst_all = get_registers_from_table(conn, 'don', '1')

#lst = get_registers_from_table_with_PK(conn, 'don', '1')
#print(f'{lst}')
#data_insertion_removal.db_clear_register_on_table_on_cascade(conn, 'don', {"id_d": 5})
#data_insertion_removal.db_clear_table_on_cascade(conn, 'don')
connection.close_connection(conn)