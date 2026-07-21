from api.external_api_testing.get_users import fetch_users
from api.api_tests import test_get_users
from database.db_connection import connect_db
from validation.validator import validate_user


def run_api_tests(records):
    """Runs the API tests and adds the results."""

    pass_count = 0
    fail_count = 0

    print("\n🌐 API TESTS")

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
    """Validates the users obtained from the API."""

    pass_count = 0
    fail_count = 0
    failed_tests = []

    print("\n👤 USER VALIDATION")

    for user in users:

        user_id = user.get("id")

        if not user_id:
            print("⚠️ User without ID:", user)
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
    """Saves the results in the database."""

    if not records:
        print("⚠️ There are no results to save.")
        return

    cursor.executemany(query, records)
    conn.commit()

    print(f"\n💾 {len(records)} results stored in the database.")


def print_report(pass_count, fail_count, failed_tests):
    """Prints the final report."""

    total = pass_count + fail_count

    print("\n📊 TEST REPORT")
    print(f"Total: {total}")
    print(f"PASS : {pass_count}")
    print(f"FAIL : {fail_count}")

    if total > 0:
        success_rate = (pass_count / total) * 100
        print(f"📈 Success: {success_rate:.2f}%")

    if failed_tests:

        print("\n❌ FAILED TESTS")

        for user_id, test_name, message in failed_tests:

            print(f"User : {user_id}")
            print(f"Test    : {test_name}")
            print(f"Reason  : {message}")
            print("-" * 35)

    print("\n✅ Process completed successfully")


def main():

    users = fetch_users()

    if not users:
        print("⚠️ No users were obtained from the API")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
    except Exception as e:
        print(f"❌ Error connecting to the DB: {e}")
        return

    query = """
    INSERT INTO test_results (user_id, test_name, result, message)
    VALUES (%s, %s, %s, %s)
    """

    records = []

    pass_count = 0
    fail_count = 0

    # API Tests
    api_pass, api_fail = run_api_tests(records)

    pass_count += api_pass
    fail_count += api_fail

    # User validation
    user_pass, user_fail, failed_tests = validate_users(users, records)

    pass_count += user_pass
    fail_count += user_fail

    # Save results
    try:
        save_results(cursor, conn, query, records)
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
    finally:
        cursor.close()
        conn.close()

    # Final report
    print_report(pass_count, fail_count, failed_tests)


if __name__ == "__main__":
    main()