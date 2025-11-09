import order_request
import data

# Мария Кальманович, 37-я когорта — Финальный проект. Инженер по тестированию плюс
    
    # Функция для позитивной проверки
def positive_assert(body):
        # В переменную order_response сохраняется результат запроса на создание заказа
        order_response = order_request.post_new_order(body)
    
        # Проверяется, что код ответа равен 201
        assert order_response.status_code == 201
        # В переменную order_track сохраняется track созданного заказа
        order_track = order_response.json()["track"]
    
        # В переменную new_order_response сохраняется результат запроса на получения заказа 
        new_order_response = order_request.get_order(order_track)
    
       # Проверяется, что код ответа равен 200
        assert new_order_response.status_code == 200
    

def test_create_order_and_get_it_by_track():
        positive_assert(data.order_body)