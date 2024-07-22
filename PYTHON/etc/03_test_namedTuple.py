from collections import namedtuple

Car = namedtuple('car', ['color', 'brand'])

car = Car('b', 'B')
cars = [
        Car(color='brown', brand='BMW'),
        Car(color='white', brand='Audi')
        ]

print(car.color)
