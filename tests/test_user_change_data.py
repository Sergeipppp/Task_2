import requests
import data
import allure
from helpers import MakeTestData

class TestUserChangeData:
    @allure.title('Проверяем изменение данных пользователя с корректным авторизационным токеном')
    def test_user_change_data_with_authtorization(self, create_data_for_user):
        response = requests.post(data.Urls.register_user, data=create_data_for_user)
        headers = {
        "Authorization": response.json()["accessToken"],
        "Content-Type": "application/json"
        }
        payload = {
            "name": MakeTestData.generate_random_string(10)
        }
        response = requests.patch(data.Urls.user, json=payload, headers=headers)
        assert response.status_code == 200 and response.json()["user"]["name"] == payload["name"]

    def test_user_change_data_without_authtorization(self, create_data_for_user):
        requests.post(data.Urls.register_user, data=create_data_for_user)
        payload = {
            "email": f"{MakeTestData.generate_random_string(10)}@yandex.ru",
            "name": MakeTestData.generate_random_string(10)
        }
        response = requests.patch(data.Urls.user, json=payload)
        assert response.status_code == 401 and response.json()["message"] == data.Answers.not_autorized_401
