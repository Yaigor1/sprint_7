import pytest
import data
import courier_api

@pytest.fixture
def new_courier():
    courier = courier_api.register_new_courier_and_return_login_password(data.needed_length)
    yield courier
    courier_api.delete_courier(courier)