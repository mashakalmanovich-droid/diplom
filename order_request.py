# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставялем полный url
                         json=body,  # подставляем наше тело
                         headers=data.headers)  # подставляем хедеры

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                         params={"t": track})