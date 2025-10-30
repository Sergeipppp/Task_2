import requests
import data
import allure

class TestLoginUser:
    @allure.title('Проверяем логин пользователя с корректными данными')
    def test_login_user_with_correct_data(self, create_data_for_user):
        requests.post(data.Urls.register_user, data=create_data_for_user)
        payload = {
            "email": create_data_for_user["email"],
            "password": create_data_for_user["password"]
        }
        response = requests.post(data.Urls.login_user, data=payload)
        assert response.status_code == 200 and response.json()["user"]["email"] == payload["email"]

    @allure.title('Проверяем логин пользователя с некорректными данными')
    def test_login_user_with_incorrect_data(self, create_data_for_user):
        requests.post(data.Urls.register_user, data=create_data_for_user)
        payload = {
            "email": "testincorrect",
            "password": "testincorrect"
        }
        response = requests.post(data.Urls.login_user, data=payload)
        assert response.status_code == 401 and response.json()["message"] == data.Answers.response_401_login
