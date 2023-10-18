import sender_stand_request
import data
import configuration
import requests

#Функция на создание заказа и получение номера трекера
def get_new_orders():
    response = sender_stand_request.post_new_orders(data.user_body)
    track_number = response.json()["track"]
    return track_number


#Функция получения заказа по треку заказа
def get_order():
    track_number = get_new_orders() #cоздание заказа и получение номера трека
    response = requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDERS + str(track_number))
    return response.status_code

def test_get_order():
    assert get_order() == 200


# Токарева Александра, 9-я когорта - Финальный проект, Инженер по тестированию плюс