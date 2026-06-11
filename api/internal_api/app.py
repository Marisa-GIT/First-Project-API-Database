from flask import Flask, request, jsonify
from database.db_connection import connect_db
import logging

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API funcionando"})

logging.basicConfig(
    filename="logs/api_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Endpoint GET
@app.route("/users", methods=["GET"])
def get_users():

    conn = connect_db()

    if conn is None:
        return jsonify({"error": "Error de conexión a la base de datos"}), 500

    try:
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return jsonify(users), 200

    except Exception:
        logging.exception("Error obteniendo usuarios")
        return jsonify({"error": "Error interno"}), 500

    finally:
        if conn:
            conn.close()
            
            cursor.close()
            conn.close()


# Endpoint POST
@app.route("/users", methods=["POST"])
def create_user():

    conn = connect_db()

    if conn is None:
        return jsonify({"error": "Error de conexión a la base de datos"}), 500

    conn = None

    try:
        if not request.is_json:
            return jsonify({"error": "Formato JSON requerido"}), 400

        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        username = data.get("username")

        if not email:
            return jsonify({"error": "Email es obligatorio"}), 400

        if "@" not in email:
            return jsonify({"error": "Email inválido"}), 400

        if not username:
            return jsonify({"error": "Username es obligatorio"}), 400

        conn = connect_db()

        if conn is None:
            return jsonify({"error": "Error DB"}), 500

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            return jsonify({"error": "Username ya existe"}), 409

        cursor.execute(
            "INSERT INTO users (name, email, username, valid) VALUES (%s, %s, %s, %s)",
            (name, email, username, True)
        )

        conn.commit()

        return jsonify({"message": "Usuario creado"}), 201

    except Exception:
        logging.exception("Error creando usuario")
        return jsonify({"error": "Error interno"}), 500

    finally:
        if conn:
            conn.close()
            
            cursor.close()
            conn.close()
# Endpoint PUT
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    conn = connect_db()
    if conn is None:
        return jsonify({"error": "Error de conexión a la base de datos"}), 500

    conn = None

    try:
        data = request.json

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        query = """
        UPDATE users
        SET name=%s, email=%s, username=%s
        WHERE id=%s
        """

        cursor.execute(query, (
            data.get("name"),
            data.get("email"),
            data.get("username"),
            user_id
        ))

        conn.commit()

        return jsonify({"message": "Usuario actualizado"}), 200

    except Exception as e:
        logging.error(f"Error actualizando usuario: {e}")
        return jsonify({"error": "Error interno"}), 500

    finally:
        if conn:
            conn.close()
            
            cursor.close()
            conn.close()

#  Endpoint DELETE
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    conn = connect_db()

    if conn is None:
        return jsonify({"error": "Error de conexión a la base de datos"}), 500

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()

        return jsonify({"message": "Usuario eliminado"}), 200

    except Exception:
        logging.exception("Error eliminando usuario")
        return jsonify({"error": "Error interno"}), 500

    finally:
        if conn:
            conn.close()

            cursor.close()
            conn.close()


if __name__ == "__main__":
    app.run(debug=True, port=5000)