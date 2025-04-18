import allure

from src.scooter_api import ScooterAPI


class TestLoginCourier:
    @allure.title('Успешный запрос на получение заказов курьера возвращает список заказов')
    def test_get_order_return_order(self):
        request = ScooterAPI()
        get_response = request.get_order_test()
        assert get_response.json()['orders']
