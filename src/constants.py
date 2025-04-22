from faker import Faker


class Url:
    COURIER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    ORDER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'


class CourierData:
        fake = Faker('ru_RU')
        USER_DATA = {
            'login': fake.unique.first_name(),
            'password': fake.unique.password(),
            'first_name' : fake.unique.first_name()
        }

        NONEXISTENT_USER_DATA = {
            'login': 'UserXXX',
            'password': 'qwerty12345',
            'first_name' : 'Alexandr'
        }


class OrderData:
    fake = Faker('ru_RU')
    USER_DATA = {
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'address': fake.address(),
        'metrostation_one': 4,
        'metrostation_two': 7,
        'metrostation_three': 14,
        'metrostation_four': 23,
        'phone': fake.phone_number(),
        'renttime_one': 0,
        'renttime_two': 1,
        'renttime_three': 2,
        'renttime_four': 3,
        'deliverydate': fake.date(),
        'comment': fake.text(max_nb_chars=80),
        'color_black': ['BLACK'],
        'color_grey': ['GREY'],
        'color_black_and_grey': ['BLACK', 'GREY']
    }
