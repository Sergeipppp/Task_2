from helpers import MakeTestData
from data import Urls
import requests
import pytest

@pytest.fixture
def create_data_for_user():
    email = MakeTestData.generate_random_string(10)
    password = MakeTestData.generate_random_string(10)
    name = MakeTestData.generate_random_string(10)

    payload = {
        "email": f"{email}@yandex.ru",
        "password": password,
        "name": name
    }
    yield payload   
    response = requests.post(Urls.login_user, data=payload)
    headers = {
        "Authorization": response.json()["accessToken"],
        "Content-Type": "application/json"
    }
    requests.delete(Urls.user, json=payload, headers=headers)
