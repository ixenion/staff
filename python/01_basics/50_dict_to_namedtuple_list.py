from collections import namedtuple

# Создаем класс "Point" с полями "x" и "y"
Point = namedtuple('Point', ['x', 'y'])

_d = {
        "a":1,
        "b":2,
        }

# Создаем экземпляр namedtuple с координатами (3, 4)
dd = list(_d.items())
pp = []
for d in dd:
    p = Point(*d)
    pp.append(p)

print(pp[0].x)
print(pp[0].y)

# p = Point(*[3, 4])
# # Мы можем обратиться к полям по их именам
# print(f"x: {p.x}, y: {p.y}")
# # Мы также можем получить элементы по индексу, как в обычном кортеже
# print(f"Элемент по индексу 0: {p[0]}")



