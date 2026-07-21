from api.external_api_testing.get_users import fetch_users
from database.db_connection import connect_db
from validation.validator import validate_user


def insert_users():

    users = fetch_users()

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO users (id, name, email, username, valid)
    VALUES (%s, %s, %s, %s, %s)
    """

    for user in users:

        is_valid, validation_results = validate_user(user)

        values = (
            user["id"],
            user["name"],
            user["email"],
            user["username"],
            is_valid
        )

        cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    print("Usuarios insertados correctamente")

