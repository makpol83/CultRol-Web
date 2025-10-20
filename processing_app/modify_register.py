import psycopg
import connection
import data_insertion_removal
import get_registers
from psycopg import sql
from enums_dicts import PRIMARY_KEYS

def db_modify_register_with_PK(conn, table_name, column_name, new_value, primary_keys: list):
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

        query = sql.SQL("UPDATE {table} SET {column} = {value_changed} WHERE {where};").format(
            table = sql.Identifier(table_name),
            column = sql.Identifier(column_name),
            where = where_clause
        )

        cur.execute(query, (new_value, *primary_keys))
        
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
lst = get_registers.get_registers_from_table_with_PK(conn, 'don', ['14'])
print(f'{lst}')
db_modify_register_with_PK(conn, 'don', 'name', '\'KKKKKKKKKKK?\'', ['14'])
lst = get_registers.get_registers_from_table_with_PK(conn, 'don', ['14'])
print(f'{lst}')
#data_insertion_removal.db_clear_register_on_table_on_cascade(conn, 'don', {"id_d": 5})
#data_insertion_removal.db_clear_table_on_cascade(conn, 'don')
connection.close_connection(conn)