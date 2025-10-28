from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permette richieste JS dal frontend

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/eventi', methods=['GET'])
def get_eventi():
    conn = get_db_connection()
    eventi = conn.execute("SELECT * FROM eventi").fetchall()
    conn.close()

    eventi_list = [
        {
            "id": e["id"],
            "titolo": e["titolo"],
            "descrizione": e["descrizione"],
            "data": e["data"],
            "ora": e["ora"]
        }
        for e in eventi
    ]

    return jsonify(eventi_list)

if __name__ == "__main__":
    app.run(debug=True)
