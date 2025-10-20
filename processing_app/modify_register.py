import psycopg
import connection
import data_insertion_removal
import get_registers
from enums_dicts import PRIMARY_KEYS

def db_modify_register_with_PK(conn, table_name, column_name, new_value, primary_keys: list):
    # We configure row_factory to access name per column
    conn.row_factory = psycopg.rows.dict_row
    cur = conn.cursor()
    
    try:
        cur.execute("BEGIN;")
        query = "UPDATE " + table_name + " SET "  + column_name + " = " + new_value + " WHERE "

        lst = PRIMARY_KEYS[table_name]
        length = len(primary_keys)
        if len(lst) != length:
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
        cur.execute("COMMIT;")
        
    except Exception as e:
        print(f"Error when modifying register from {table_name}: {e}")
        return []
    finally:
        cur.close()

# debug functions
conn = connection.create_connection()
#data_insertion_removal.db_insert_register_on_table(conn, ['don', 'name', 'EE_use', 'description'], ['DON_TEST', '15', 'DESCR_TEST'])
#data_insertion_removal.db_insert_register_on_table(conn, ['don', 'name', 'EE_use', 'description'], ['DON_TEST', '16', 'DESCR_TEST'])
#lst_all = get_registers.get_registers_from_table(conn, 'don')
#print(f'{lst_all}')
#lst = get_registers.get_registers_from_table_with_PK(conn, 'don', ['14'])
#print(f'{lst}')
#db_modify_register_with_PK(conn, 'don', 'name', '\'TEST_CHANGES?\'', ['14'])
#lst = get_registers.get_registers_from_table_with_PK(conn, 'don', ['14'])
#print(f'{lst}')
#data_insertion_removal.db_clear_register_on_table_on_cascade(conn, 'don', {"id_d": 5})
#data_insertion_removal.db_clear_table_on_cascade(conn, 'don')
connection.close_connection(conn)