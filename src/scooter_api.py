import email

import requests
import allure

from src.constants import Url


class ScooterAPI:
    @allure.step('Запрос создания курьера')
    def create_courier(self, login, password, firstname):
        data = {'login': login, 'password': password, 'firstName': firstname}
        response = requests.post(Url.COURIER_URL, json=data)
        return response

    @allure.step('Запрос авторизации курьера')
    def login_courier(self, login, password, firstname):
        data = {'login': login, 'password': password, 'firstName': firstname}
        response = requests.post(f'{Url.COURIER_URL}/login', json=data)
        return response

    @allure.step('Запрос удаления курьера')
    def delete_courier(self, id):
        response = requests.delete(f'{Url.COURIER_URL}/{id}')
        return response

    @allure.step('Запрос создания заказа')
    def create_order(self, firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment, color):
        data = {'firstName': firstname, 'lastName': lastname, 'address': address, 'metroStation': metrostation,
                'phone': phone, 'rentTime': renttime, 'deliveryDate': deliverydate, 'comment': comment,
                'color': color}
        response = requests.post(f'{Url.ORDER_URL}', json=data)
        return response

    @allure.step('Запрос отмены заказа')
    def cancel_order(self, track):
        data = {'track': track}
        response = requests.put(f'{Url.ORDER_URL}/cancel', json=data)
        return response

    @allure.step('Запрос получение заказов')
    def get_order(self, id):
        response = requests.get(f'{Url.ORDER_URL}?courierId={id}')
        return response

    @allure.step('Запрос получение заказов')
    def get_order_test(self):
        response = requests.get(f'{Url.ORDER_URL}')
        return response