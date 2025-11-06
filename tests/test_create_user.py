import requests
import data
import allure
import pytest
from helpers import MakeTestData

class TestCreateUser:
    @allure.title('Регистрируем нового пользователя с новыми данными')
    def test_create_new_uniq_user(self, create_data_for_user):
        response = requests.post(data.Urls.register_user, data=create_data_for_user)
        assert response.status_code == 200 and response.json()["user"]["email"] == create_data_for_user["email"]

    @allure.title('Регистрируем нового пользователя с существующими данными')
    def test_register_new_user_with_exist_data(self, create_data_for_user):
        requests.post(data.Urls.register_user, data=create_data_for_user)           
        response = requests.post(data.Urls.register_user, data=create_data_for_user)
        assert response.status_code == 403 and response.json()["message"] == data.Answers.response_403_user_exist
  
    @allure.title('Регистрируем нового пользователя без обязательного поля (по очереди проверяем отсутствие email, password, name)')
    @pytest.mark.parametrize(
    'key0,key1',
    [
        ["email", "password"],
        ["email", "name"],
        ["password", "name"]
    ])
    def test_register_new_user_without_some_field(self, key0, key1):
        response = requests.post(data.Urls.register_user, data={
            key0: f"{MakeTestData.generate_random_string(10)}@yandex.ru",
            key1: MakeTestData.generate_random_string(10)
        })
        assert response.status_code == 403 and response.json()["message"] == data.Answers.response_403_user
