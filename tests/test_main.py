from unittest.mock import MagicMock, patch

from main import main


def test_main_runs_without_errors():
    try:
        main()
    except Exception as e:
        assert False, f"main() raised an exception: {e}"


@patch("main.connect_db")
@patch("main.fetch_users")
@patch("main.test_get_users")
@patch("main.validate_user")
def test_main_success(
    mock_validate_user,
    mock_test_get_users,
    mock_fetch_users,
    mock_connect_db,
):

    # Simulated user
    mock_fetch_users.return_value = [
        {
            "id": 1,
            "name": "Test User",
            "email": "test@test.com",
            "username": "testuser",
        }
    ]

    # Simulated API results
    mock_test_get_users.return_value = [
        ("status_code", "PASS", "Status 200 OK"),
        ("response_time", "PASS", "Less than 1s"),
        ("json_format", "PASS", "Correct format"),
    ]

    # Simulated validator result
    mock_validate_user.return_value = (
        True,
        [
            ("email_format", "PASS", "Valid email"),
            ("username_length", "PASS", "Valid length"),
        ],
    )

    # Mock of the database
    mock_cursor = MagicMock()
    mock_conn = MagicMock()

    mock_conn.cursor.return_value = mock_cursor
    mock_connect_db.return_value = mock_conn

    # Execute
    main()

    # Verifications
    mock_fetch_users.assert_called_once()
    mock_test_get_users.assert_called_once()
    mock_validate_user.assert_called_once()

    mock_cursor.executemany.assert_called_once()
    mock_conn.commit.assert_called_once()

    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()