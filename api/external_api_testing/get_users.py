import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("An error occurred while consuming the API")
        return []
