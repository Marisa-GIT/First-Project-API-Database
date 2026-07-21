import requests

def test_get_users():

    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    results = []

    # Test 1: Status code
    if response.status_code == 200:
        results.append(("status_code", "PASS", "Status 200 OK"))
    else:
        results.append(("status_code", "FAIL", f"Status {response.status_code}"))

    # Test 2: Response time
    if response.elapsed.total_seconds() < 1:
        results.append(("response_time", "PASS", "Less than 1s"))
    else:
        results.append(("response_time", "FAIL", "Very slow"))

    # Test 3: JSON Structure
    try:
        data = response.json()
        if isinstance(data, list):
            results.append(("json_format", "PASS", "Correct format"))
        else:
            results.append(("json_format", "FAIL", "Not a list"))
    except:
        results.append(("json_format", "FAIL", "Not valid JSON"))

    return results