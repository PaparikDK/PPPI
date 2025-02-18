import random

class Order:
    """
    Класс для представления заказа грузоперевозки.

    Attributes:
        cargo_type (str): Тип груза.
        distance (int): Расстояние для перевозки в километрах.
        payment (float): Оплата за перевозку.

    @author Danil Kravchuk
    @version 1.0.1
    @copyright GNU Public License
    @todo реализовать все методы
    """

    def __init__(self, cargo_type, distance, payment):
        """
        Инициализирует новый заказ.

        Args:
            cargo_type (str): Тип груза.
            distance (int): Расстояние в километрах.
            payment (float): Оплата за перевозку.
        """
        self.cargo_type = cargo_type
        self.distance = distance
        self.payment = payment

    def __str__(self):
        """
        Возвращает строковое представление заказа.

        Returns:
            str: Информация о заказе.
        """
        return f"Заказ: {self.cargo_type}, Расстояние: {self.distance} км, Оплата: {self.payment:.2f} руб."


def generate_order():
    """
    Генерирует новый заказ с случайным типом груза и расстоянием.

    Returns:
        Order: Новый созданный заказ.
    """
    cargo_types = ['фрукты', 'стройматериалы', 'техника', 'нефть']
    distance = random.randint(50, 1000)  # расстояние от 50 до 1000 км
    payment = distance * random.uniform(0.5, 2.0)  # оплата зависит от расстояния
    cargo_type = random.choice(cargo_types)

    return Order(cargo_type, distance, payment)


class OrderManager:
    """
    Класс для управления заказами.

    Attributes:
        orders (list): Список всех заказов.
    """

    def __init__(self):
        """
        Инициализирует экземпляр OrderManager с пустым списком заказов.
        """
        self.orders = []

    def add_order(self, order):
        """
        Добавляет новый заказ в список заказов.

        Args:
            order (Order): Заказ, который необходимо добавить.
        """
        self.orders.append(order)

    def show_orders(self):
        """
        Отображает все заказы в списке.
        """
        for order in self.orders:
            print(order)

# Пример использования
if __name__ == "__main__":
    order_manager = OrderManager()

    for _ in range(5):  # Генерируем 5 случайных заказов
        new_order = generate_order()
        order_manager.add_order(new_order)

    print("Список всех заказов:")
    order_manager.show_orders()


