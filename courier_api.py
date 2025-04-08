import requests
import allure
from helper import generate_random_string

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

@allure.step("Регистрация нового курьера")
def register_new_courier_and_return_login_password(wanted_length):
    login_pass = []

    login = generate_random_string(wanted_length)
    password = generate_random_string(wanted_length)
    first_name = generate_random_string(wanted_length)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(BASE_URL, json=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return login_pass

def get_courier_id(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(f'{BASE_URL}/login', json=payload)

    if response.status_code == 200:
        text_response = response.json()
        return text_response.get('id')
    return None

def delete_courier_by_id(courier_id):
    if courier_id:
        requests.delete(f'{BASE_URL}/{courier_id}')

@allure.step("Удаление курьера")
def delete_courier(courier_existed):
    courier_id = get_courier_id(courier_existed[0], courier_existed[1])
    delete_courier_by_id(courier_id)

@allure.step("Логин и удаление курьера")
def created_courier_login_and_delete(payload):
    courier_id = get_courier_id(payload["login"], payload["password"])
    delete_courier_by_id(courier_id)