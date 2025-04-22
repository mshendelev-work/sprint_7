import allure
import pytest

from src.scooter_api import ScooterAPI

context = {}

@pytest.fixture
@allure.step('Удаление тестовых данных после создания курьера')
def delete_data_after_create():
    yield
    login = context.get('login')
    password = context.get('password')
    firstname = context.get('firstname')
    request = ScooterAPI()
    login_response = request.login_courier(login, password, firstname)
    assert login_response.status_code == 200
    id = login_response.json()['id']
    delete_response = request.delete_courier(id)
    assert delete_response.status_code == 200

@pytest.fixture
@allure.step('Удаление курьера после логина')
def delete_data_after_login():
    yield
    request = ScooterAPI()
    id = context.get('id')
    delete_response = request.delete_courier(id)
    assert delete_response.status_code == 200

@pytest.fixture
@allure.step('Отмена заказа')
def cancel_order():
    yield
    request = ScooterAPI()
    track = context.get('track')
    cancel_response = request.cancel_order(track)
    assert cancel_response.status_code == 200
