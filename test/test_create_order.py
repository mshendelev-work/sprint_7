import allure
import pytest

from conftest import context
from src.constants import OrderData
from src.scooter_api import ScooterAPI


class TestCreateOrder:
    @allure.title('Успешное создание заказа возвращает код ответа 201')
    @pytest.mark.parametrize('firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment, color',
         [(OrderData.USER_DATA['firstname'], OrderData.USER_DATA['lastname'],
           OrderData.USER_DATA['address'], OrderData.USER_DATA['metrostation_one'], OrderData.USER_DATA['phone'],
           OrderData.USER_DATA['renttime_one'], OrderData.USER_DATA['deliverydate'], OrderData.USER_DATA['comment'],
           OrderData.USER_DATA['color_black']),
          (OrderData.USER_DATA['firstname'], OrderData.USER_DATA['lastname'],
           OrderData.USER_DATA['address'], OrderData.USER_DATA['metrostation_two'], OrderData.USER_DATA['phone'],
           OrderData.USER_DATA['renttime_two'], OrderData.USER_DATA['deliverydate'], OrderData.USER_DATA['comment'],
           OrderData.USER_DATA['color_grey']),
          (OrderData.USER_DATA['firstname'], OrderData.USER_DATA['lastname'],
           OrderData.USER_DATA['address'], OrderData.USER_DATA['metrostation_three'], OrderData.USER_DATA['phone'],
           OrderData.USER_DATA['renttime_three'], OrderData.USER_DATA['deliverydate'], OrderData.USER_DATA['comment'],
           OrderData.USER_DATA['color_black_and_grey']),
          (OrderData.USER_DATA['firstname'], OrderData.USER_DATA['lastname'],
           OrderData.USER_DATA['address'], OrderData.USER_DATA['metrostation_four'], OrderData.USER_DATA['phone'],
           OrderData.USER_DATA['renttime_four'], OrderData.USER_DATA['deliverydate'], OrderData.USER_DATA['comment'],
           [''])])
    def test_create_order_return_201(self, firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment,
                          color, cancel_order):
        request = ScooterAPI()
        create_response = request.create_order(firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment,
                          color)
        context['track'] = create_response.json()['track']
        assert create_response.status_code == 201

    @allure.title('Успешное создание заказа возвращает "track"')
    @pytest.mark.parametrize('firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment, color',
         [(OrderData.USER_DATA['firstname'], OrderData.USER_DATA['lastname'],
           OrderData.USER_DATA['address'], OrderData.USER_DATA['metrostation_one'], OrderData.USER_DATA['phone'],
           OrderData.USER_DATA['renttime_one'], OrderData.USER_DATA['deliverydate'], OrderData.USER_DATA['comment'],
           OrderData.USER_DATA['color_black']),
          (OrderData.USER_DATA['firstname'], OrderData.USER_DATA['lastname'],
           OrderData.USER_DATA['address'], OrderData.USER_DATA['metrostation_two'], OrderData.USER_DATA['phone'],
           OrderData.USER_DATA['renttime_two'], OrderData.USER_DATA['deliverydate'], OrderData.USER_DATA['comment'],
           OrderData.USER_DATA['color_grey']),
          (OrderData.USER_DATA['firstname'], OrderData.USER_DATA['lastname'],
           OrderData.USER_DATA['address'], OrderData.USER_DATA['metrostation_three'], OrderData.USER_DATA['phone'],
           OrderData.USER_DATA['renttime_three'], OrderData.USER_DATA['deliverydate'], OrderData.USER_DATA['comment'],
           OrderData.USER_DATA['color_black_and_grey']),
          (OrderData.USER_DATA['firstname'], OrderData.USER_DATA['lastname'],
           OrderData.USER_DATA['address'], OrderData.USER_DATA['metrostation_four'], OrderData.USER_DATA['phone'],
           OrderData.USER_DATA['renttime_four'], OrderData.USER_DATA['deliverydate'], OrderData.USER_DATA['comment'],
           [''])])
    def test_create_order_return_track(self, firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment,
                          color, cancel_order):
        request = ScooterAPI()
        create_response = request.create_order(firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment,
                          color)
        context['track'] = create_response.json()['track']
        assert create_response.json()['track']
