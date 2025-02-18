import random

class Order:
    def __init__(self, cargo_type, distance, payment):
        self.cargo_type = cargo_type
        self.distance = distance
        self.payment = payment

def generate_order():
    cargo_types = ['фрукты', 'стройматериалы', 'техника', 'нефть']
    distance = random.randint(50, 1000)                                 # расстояние от 50 до 1000 км
    payment = distance * random.uniform(0.5, 2.0)                       # оплата зависит от расстояния
    cargo_type = random.choice(cargo_types)
    
    return Order(cargo_type, distance, payment)

new_order = generate_order()
print(f"Заказ: {new_order.cargo_type}, Расстояние: {new_order.distance} км, Оплата: {new_order.payment:.2f} руб.")
