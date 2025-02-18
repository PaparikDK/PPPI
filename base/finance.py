import random

class Order:
    """
    Класс для представления заказа грузоперевозки.

    Attributes:
        cargo_type (str): Тип груза.
        distance (int): Расстояние для перевозки в километрах.
        payment (float): Оплата за перевозку.
    """

    def __init__(self, cargo_type, distance, payment):
        """
        Инициализация нового заказа.

        Args:
            cargo_type (str): Тип груза для заказа.
            distance (int): Расстояние для перевозки в километрах.
            payment (float): Оплата за перевозку.
        """
        self.cargo_type = cargo_type
        self.distance = distance
        self.payment = payment

def generate_order():
    """
    Генерирует новый заказ с случайным типом груза и расстоянием.

    Randomly selects a cargo type from a predefined list, generates a distance
    between 50 and 1000 kilometers, and calculates the payment based on the distance.

    Returns:
        Order: Новый созданный заказ с заданными параметрами.
    """
    cargo_types = ['фрукты', 'стройматериалы', 'техника', 'нефть']
    distance = random.randint(50, 1000)   # расстояние от 50 до 1000 км
    payment = distance * random.uniform(0.5, 2.0)  # оплата зависит от расстояния
    cargo_type = random.choice(cargo_types)

    return Order(cargo_type, distance, payment)

# Генерация нового заказа
new_order = generate_order()
print(f"Заказ: {new_order.cargo_type}, Расстояние: {new_order.distance} км, Оплата: {new_order.payment:.2f} руб.")

