import requests
import data
import allure

class TestUserGetOrder:
    @allure.title('Проверяем получения списока заказов с авторизационным токеном')
    def test_user_with_autorization_get_order(self, create_data_for_user):
        response = requests.post(data.Urls.register_user, data=create_data_for_user)
        headers = {
        "Authorization": response.json()["accessToken"],
        "Content-Type": "application/json"
        }
        response1 = requests.get(data.Urls.ingredients)
        payload = {
            "ingredients": [response1.json()["data"][0]["_id"]]
        }
        requests.post(data.Urls.order, json=payload, headers=headers)
        response2 = requests.get(data.Urls.order, headers=headers)
        assert response2.status_code == 200 and response2.json()["orders"][0]["ingredients"] == payload["ingredients"]

    @allure.title('Проверяем получения списока заказов с авторизационным токеном')
    def test_user_without_autorization_get_order(self):
        response = requests.get(data.Urls.order)
        assert response.status_code == 401 and response.json()["message"] == data.Answers.not_autorized_401
