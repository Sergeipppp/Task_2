from dataclasses import dataclass

@dataclass
class Answers:
    response_403_user_exist = "User already exists"
    response_403_user = "Email, password and name are required fields"
    response_401_login = "email or password are incorrect"
    not_autorized_401 = "You should be authorised"
    empty_ingredient = "Ingredient ids must be provided"

@dataclass
class Urls:
    base_url = "https://stellarburgers.education-services.ru/api"
    register_user = f"{base_url}/auth/register"
    user = f"{base_url}/auth/user"
    login_user = f"{base_url}/auth/login"
    order = f"{base_url}/orders"
    ingredients = f"{base_url}/ingredients"
