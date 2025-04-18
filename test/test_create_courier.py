import allure

from conftest import context
from src.constants import CourierData
from src.helpers import register_new_courier_and_return_login_password, register_new_courier_and_return_response
from src.scooter_api import ScooterAPI


class TestCreateCourier:
    @allure.title('Успешный запрос создание курьера возвращает код ответа 201')
    def test_signup_return_201(self, delete_data_after_create):
        signup_response = register_new_courier_and_return_response()
        assert signup_response.status_code == 201

    @allure.title('Успешный запрос создание курьера возвращает {{"ok":true}}')
    def test_signup_return_ok_true(self, delete_data_after_create):
        signup_response = register_new_courier_and_return_response()
        assert signup_response.text == '{"ok":true}'

    @allure.title('Попытка создания двух одинаковых курьеров возвращает код ответа 409')
    def test_identical_signup_return_409(self, delete_data_after_create):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        signup_response = request.create_courier(context['login'], context['password'], context['firstname'])
        assert signup_response.status_code == 409

    @allure.title('Попытка создания двух одинаковых курьеров возвращает "Этот логин уже используется. Попробуйте другой."')
    def test_identical_signup_return_fail(self, delete_data_after_create):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        signup_response = request.create_courier(context['login'], context['password'], context['firstname'])
        assert signup_response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Попытка создания курьера c пустым логином возвращает код ответа 400')
    def test_signup_with_empty_login_return_400(self):
        login = ''
        password = CourierData.USER_DATA['password']
        firstname = CourierData.USER_DATA['first_name']
        request = ScooterAPI()
        signup_response = request.create_courier(login, password, firstname)
        assert signup_response.status_code == 400

    @allure.title('Попытка создания курьера c пустым паролем возвращает "Недостаточно данных для создания учетной записи"')
    def test_signup_with_empty_password_return_fail(self):
        login = CourierData.USER_DATA['login']
        password = ''
        firstname = CourierData.USER_DATA['first_name']
        request = ScooterAPI()
        signup_response = request.create_courier(login, password, firstname)
        assert signup_response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Попытка создания курьера c повторяющимся логином возвращает код ответа 409')
    def test_signup_double_login_return_409(self, delete_data_after_create):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        signup_response = request.create_courier(context['login'], context['password'], context['firstname'])
        assert signup_response.status_code == 409

    @allure.title('Попытка создания курьера c повторяющимся логином возвращает "Этот логин уже используется. Попробуйте другой."')
    def test_signup_double_login_return_fail(self, delete_data_after_create):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        signup_response = request.create_courier(context['login'], context['password'], context['firstname'])
        assert signup_response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
