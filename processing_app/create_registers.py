import connection
import data_insertion_removal
import enums_dicts

# Generic function to insert on to the table
def insert_into_table(table_name: str, data_lst: list):
    if table_name not in TABLES_COLUMNS:
        raise ValueError(f"The table '{table_name}' is not defined in TABLES_COLUMNS")
    
    table_info = TABLES_COLUMNS[table_name]
    
    conn = connection.create_connection()
    data_insertion_removal.db_insert_register_on_table(conn, table_info, data_lst)
    connection.close_connection(conn)