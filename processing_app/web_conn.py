from flask import Flask, jsonify
from db import connection, get_registers

app = Flask(__name__)

@app.route("/api/data", methods=["GET"])
def api_get_TEST():
    try:
        conn = connection.create_connection()
        all_data = get_registers.get_registers_from_table(conn, 'don')
        print(f'{all_data}')
        data = get_registers.get_registers_from_table_with_PK(conn, 'don', ['14'])
        print(f'{data}')
        # convierte a JSON
        connection.close_connection(conn)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

