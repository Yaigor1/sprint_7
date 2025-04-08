import requests

class TestCourierLogin:

    def test_courier_login_with_all_fields_success_and_return_id(self, new_courier):
        payload = {"login": new_courier[0], "password": new_courier[1]}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        code_response = response.status_code
        text_response = response.json()
        courier_id = text_response.get('id')
        assert code_response == 200 and isinstance(courier_id, int)

    def test_courier_login_with_incorrect_login_failed(self, new_courier):
        payload = {"login": "wrong_login", "password": new_courier[1]}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        code_response = response.status_code
        text_response = response.json()
        assert code_response == 404 and text_response["message"] == "Учетная запись не найдена"

    def test_courier_login_with_incorrect_password_failed(self, new_courier):
        payload = {"login": new_courier[0], "password": "wrong_password"}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        code_response = response.status_code
        text_response = response.json()
        assert code_response == 404 and text_response["message"] == "Учетная запись не найдена"

    def test_courier_login_without_login_failed(self, new_courier):
        payload = {"login": None, "password": new_courier[1]}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        code_response = response.status_code
        text_response = response.json()
        assert code_response == 400 and text_response["message"] == "Недостаточно данных для входа"

    def test_courier_login_without_password_failed(self, new_courier):
        payload = {"login": new_courier[0], "password": ""}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        code_response = response.status_code
        text_response = response.json()
        assert code_response == 400 and text_response["message"] == "Недостаточно данных для входа"