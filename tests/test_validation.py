from api.internal_api.app import app

def test_validate_without_data():

    client = app.test_client()

    response = client.post(
        "/validate",
        json={}
    )

    assert response.status_code in [400, 422]