from api.external_api_testing.get_users import fetch_users
from api.api_tests import test_get_users
from database.db_connection import connect_db
from validation.validator import validate_user


def run_api_tests(records):
    """Ejecuta las pruebas de la API y agrega los resultados."""

    pass_count = 0
    fail_count = 0

    print("\n🌐 TESTS DE API")

    api_results = test_get_users()

    for test_name, result, message in api_results:

        print(test_name, result, message)

        if result == "PASS":
            pass_count += 1
        else:
            fail_count += 1

        records.append((None, test_name, result, message))

    return pass_count, fail_count


def validate_users(users, records):
    """Valida los usuarios obtenidos desde la API."""

    pass_count = 0
    fail_count = 0
    failed_tests = []

    print("\n👤 VALIDACIÓN DE USUARIOS")

    for user in users:

        user_id = user.get("id")

        if not user_id:
            print("⚠️ Usuario sin ID:", user)
            continue

        _, test_results = validate_user(user)

        for test_name, result, message in test_results:

            if result == "PASS":
                pass_count += 1
            else:
                fail_count += 1
                failed_tests.append((user_id, test_name, message))

            records.append((user_id, test_name, result, message))

    return pass_count, fail_count, failed_tests


def save_results(cursor, conn, query, records):
    """Guarda los resultados en la base de datos."""

    if not records:
        print("⚠️ No hay resultados para guardar.")
        return

    cursor.executemany(query, records)
    conn.commit()

    print(f"\n💾 {len(records)} resultados almacenados en la base de datos.")


def print_report(pass_count, fail_count, failed_tests):
    """Imprime el reporte final."""

    total = pass_count + fail_count

    print("\n📊 REPORTE DE PRUEBAS")
    print(f"Total: {total}")
    print(f"PASS : {pass_count}")
    print(f"FAIL : {fail_count}")

    if total > 0:
        success_rate = (pass_count / total) * 100
        print(f"📈 Éxito: {success_rate:.2f}%")

    if failed_tests:

        print("\n❌ PRUEBAS FALLIDAS")

        for user_id, test_name, message in failed_tests:

            print(f"Usuario : {user_id}")
            print(f"Test    : {test_name}")
            print(f"Motivo  : {message}")
            print("-" * 35)

    print("\n✅ Proceso finalizado correctamente")


def main():

    users = fetch_users()

    if not users:
        print("⚠️ No se obtuvieron usuarios desde la API")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
    except Exception as e:
        print(f"❌ Error conectando a la DB: {e}")
        return

    query = """
    INSERT INTO test_results (user_id, test_name, result, message)
    VALUES (%s, %s, %s, %s)
    """

    records = []

    pass_count = 0
    fail_count = 0

    # Tests de API
    api_pass, api_fail = run_api_tests(records)

    pass_count += api_pass
    fail_count += api_fail

    # Validación de usuarios
    user_pass, user_fail, failed_tests = validate_users(users, records)

    pass_count += user_pass
    fail_count += user_fail

    # Guardar resultados
    try:
        save_results(cursor, conn, query, records)
    except Exception as e:
        print(f"❌ Error insertando datos: {e}")
    finally:
        cursor.close()
        conn.close()

    # Reporte final
    print_report(pass_count, fail_count, failed_tests)


if __name__ == "__main__":
    main()