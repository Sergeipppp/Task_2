import requests
import data
import allure

class TestCreateOrders:
    @allure.title('Проверяем создание заказа с авторизационным токеном и ингредиентами')
    def test_create_orders_with_authorization(self, create_data_for_user):
        response = requests.post(data.Urls.register_user, data=create_data_for_user)
        headers = {
        "Authorization": response.json()["accessToken"],
        "Content-Type": "application/json"
        }
        response1 = requests.get(data.Urls.ingredients)
        payload = {
            "ingredients": [response1.json()["data"][0]["_id"]]
        }
        response2 = requests.post(data.Urls.order, json=payload, headers=headers)
        assert response2.status_code == 200 and response2.json()["success"] == True

    @allure.title('Проверяем создание заказа без авторизационного токена и ингредиентами')
    def test_create_orders_without_authorization(self):
        response = requests.get(data.Urls.ingredients)
        payload = {
            "ingredients": [response.json()["data"][0]["_id"]]
        }
        response1 = requests.post(data.Urls.order, json=payload)
        assert response1.status_code == 200 and response1.json()["success"] == True

    @allure.title('Проверяем создание заказа без авторизационного токена и без ингредиентов')
    def test_create_orders_without_ingredients(self):
        response = requests.post(data.Urls.order)
        assert response.status_code == 400 and response.json()["message"] == data.Answers.empty_ingredient

    @allure.title('Проверяем создание заказа без авторизационного токена и с некорректным хешем ингредиента')
    def test_create_orders_with_incorrect_hash_of_ingredient(self):
        payload = {
            "ingredients": ["123"]
        }
        response = requests.post(data.Urls.order, json=payload)
        assert response.status_code == 500
