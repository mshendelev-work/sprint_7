import allure

from conftest import context
from src.constants import CourierData
from src.helpers import register_new_courier_and_return_login_password
from src.scooter_api import ScooterAPI


class TestLoginCourier:
    @allure.title('Успешный запрос на авторизацию курьера возвращает код ответа 200')
    def test_login_return_200(self, delete_data_after_login):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        login_response = request.login_courier(context['login'], context['password'], context['firstname'])
        context['id'] = login_response.json()['id']
        assert login_response.status_code == 200

    @allure.title('Успешный запрос на авторизацию курьера возвращает "id"')
    def test_login_return_id(self, delete_data_after_login):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        login_response = request.login_courier(context['login'], context['password'], context['firstname'])
        context['id'] = login_response.json()['id']
        assert login_response.json()['id']

    @allure.title('Попытка авторизации курьера с неверным паролем возвращает код ответа 404')
    def test_login_with_invalid_password_return_404(self, delete_data_after_create):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        login_response = request.login_courier(context['login'], CourierData.NONEXISTENT_USER_DATA['password'], context['firstname'])
        assert login_response.status_code == 404

    @allure.title('Попытка авторизации курьера с неверным логином возвращает "Учетная запись не найдена"')
    def test_login_with_invalid_login_return_fail(self, delete_data_after_create):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        login_response = request.login_courier(CourierData.NONEXISTENT_USER_DATA['login'], context['password'], context['firstname'])
        assert login_response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Попытка авторизация курьера c пустым логином возвращает код ответа 400')
    def test_login_courier_with_empty_login_return_400(self, delete_data_after_create):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        login_response = request.login_courier('', context['password'], context['firstname'])
        assert login_response.status_code == 400

    @allure.title('Попытка авторизация курьера c пустым паролем возвращает "Недостаточно данных для входа"')
    def test_login_courier_with_empty_password_return_fail(self, delete_data_after_create):
        courier_data = register_new_courier_and_return_login_password()
        context['login'] = courier_data[0]
        context['password'] = courier_data[1]
        context['firstname'] = courier_data[2]
        request = ScooterAPI()
        login_response = request.login_courier(context['login'], '', context['firstname'])
        assert login_response.json()['message'] == 'Недостаточно данных для входа'
