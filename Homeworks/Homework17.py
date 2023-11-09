# 17-1:
import re


def twins(s):
    pattern = r'\b(\w+)(?:\s+\1\b)+'
    new = re.sub(pattern, r'\1', s)
    return new


s = "Напишите программу программу, которая устраняет повторение " \
    "повторение слов, т.е. результат результат должен быть таким."

print(twins(s))


# 17-2:
def decorator(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapper


@decorator
def up(*args, **kwargs):
    res = []
    for x in args:
        if isinstance(x, str):
            res.append(x.upper())
    for x in kwargs.values():
        if isinstance(x, str):
            res.append(x.upper())
    print(res)


result = up('hi', 54, 'python', **{'1': 'Red', '2': "Blue", '3': 4})


# 17-3:
class Shape:
    def __init__(self, color, square):
        self.color = color
        self.shape = square

    def set_color(self):
        self.color = str(input('Введите цвет: '))

    def get_color(self):
        print(self.color)

    def set_square(self):
        self.square = int(input('Введите площадь: '))

    def get_sqyare(self):
        print(self.square)


cir = Shape("None", 0)

cir.set_color()
cir.get_color()
cir.set_square()
cir.get_sqyare()
