# print(11>0 is True)
# print(0<0 == 0)
# print(1 in range(2) = True)
# print((11>0) is True)

# # Homework
# import re
# s = 'Напишите программу программц которая устраняет повторение повторение'
# re.sub(r'(\b\w+\b\W+\1)', r'\1', s, flags = re.I)


# def deco(func):
#     def wrapper(*args, **kwargs):
#         res = []
#         for i in args:
#             if isinstance(i, str):
#                 res.append(i.upper())
#         for i in kwargs.values():
#             if isinstance(i, str):
#                 res.append(i.upper())
#         out = func(*args, **kwargs)
#         return out, res
#     return wrapper

# @deco
# def fu(*args, **kwargs):
#     return

# result = fu('первый', ['второй'], '3', 4, a='пятый', b='1111')

# print(result)


# class Figure:
#     def __init__(self, color, peri = 0):
#         self.peri = peri
#         self.color = color
# a = Figure('Red', 100)
# b = Figure('Blue')
# print(a.peri)
# print(b.peri)


# class Student:
#     lst = []
#     def __init__(self, name):
#         self.name = name
#         Student.lst.append(self.name)
#         print('The object is created!')

#     def info(self):
#         print(f'Имя: {self.name}')
#         print(Student.lst)


# def __del__(self):
#     del s1
#     print('Объект удалён!')


# s1 = Student('Ella')
# s1.info()
# s2 = Student("Sergei")
# s2.info()
# type(s1)


# class Tree(object):
#     def __init__(self, kind, height):
#         self.kind = kind
#         self.age = 0
#         self.height = height

#     def grow(self):
#         self.age += 1

# class FruitTree(Tree):
#     def __init__(self, kind, height):
#             super().__init__(kind, height)

#     def give_fruit(self):
#          print(f'20 kg of {self.kind}')

#     def give_fruit(self, how_many):
#          print(f'{how_many} kg of {self.kind}')

# # a = FruitTree('Яблоня', 1) # Метод "давать фрукты" опеределен только для объектра Tree
# # a.give_fruit()
# # b = FruitTree('Orange tree', 2)
# # # b.give_fruit() # Метод "давать фрукты" опеределен только для объектра Tree - поэтому будет ошибка
# c = FruitTree('Апельсин', 1)
# c.give_fruit(8)


# * Полиморфизм - в разных объектах одна и та же операция может выполнять различные функции
# * Инкапсуляция - можно скрыть ненужные внутренние подробности работы объекта от окружающего мира
# * Наследование - можно создать специализированные классы на основе базовых
# * Абстракция - создавать интервейсы и классы, которые определяют только те свойства и методы, которые необходимы для выоплнения определнной задачи

# * В Python, `super()` используется для вызова метода родительского класса. Он позволяет обратиться к методу, который был переопределен в дочернем классе,
# * и вызвать его родительскую реализацию. Это полезно, когда требуется расширить функциональность метода родительского класса, не повторяя его код.
# * `super()` используется внутри дочернего класса и принимает два параметра: текущий класс и текущий объект. Он возвращает специальный объект,
# * называемый "прокси-объектом", который позволяет вызывать родительский метод.


# class Figure:
#     def __init__(self, colour, perimetr):
#         self.color = colour
#         self.perimetr = perimetr

#     def set_peri(self):
#         self.perimetr = self.perimetr

#     def get_peri(self):
#         return self.perimetr


# # Наследуется от класса Figure:
# fig = Figure('Blue', 15)
# fig.set_peri()
# print(fig.get_peri())


# class Triangle(Figure):
#     def __init__(self, colour, a, b, c):
#         self.colour = colour
#         self.a = a
#         self.b = b
#         self.c = c

#     def set_peri(self):
#         self.peri = self.a + self.b + self.c

#     def get_peri(self):
#         return self.peri


# # Наследуется от класса Triangle:
# abc = Triangle('Red', 3, 4, 5)
# abc.set_peri()
# print(abc.get_peri())

# # Наследуется от класса Figure:


# class Rectangle(Figure):
#     def __init__(self, colour, length, width):
#         super().__init__(colour, ((length + width) * 2))

# # rct = Rectangle('Yellow', 2, 3)
# # print(rct.kvadrat)

# # Используем инит от класста Rectangle выше, который использует инит от класса Figure в самом верху


# class Square(Rectangle):
#     def __init__(self, colour, x):
#         super().__init__(colour, x, x)


# sqr = Square('Black', 5)
# print(sqr.perimetr)


# # Интересное множественное и многоуровневое наследование:
# class X(str):
#     def init(self, s):
#         self.s = s

#     def add(self, other):
#         return self.s + other.s

# class Y(int):
#     def init(self, s):
#         self.s = s

#     def add(self, other):
#         return self.s * other.s # Вот тут мы переопределяем сложение ниже на умножение! (P.S. 11*11 = 121, 111*111 - 12321 и т.д.)

# # В данном случае other и не нужен, но в будущем можно вместо other поставить что то другое. Но пока функцию other исполняет self

# x = X('aaa')
# z = X('bbb')
# print(x+z)

# y = Y(10)
# print(y+y) # То есть несмотря на сложение тут, все равно будет умножение в методе add

# * В данном контексте, other - это другой объект, который передается в метод add вместе с объектом, для которого
# * вызывается данный метод. В случае x+z, other будет объект класса X с атрибутом s, равным 'bbb'. В случае y+y,
# * other также будет объект класса Y с атрибутом s, равным 11. ИНЫМИ СЛОВАМИ - если нет other то он other воспринимает объект y!
# *  А если закоментить строчки def ad и ниже класса Y, то метод опять переопределиться на сложение в print(y+y)

# print(dir(int))


# +/- Homework

# class Data:
#     def init(self, *info):
#         self.info = list(info)

#     def getitem(self, i):
#         return self.info[i]

# class Teacher:
#     def init(self):
#         self.work = 0

#     def teach(self, info, *pupil):
#         for i in pupil:
#             i.take(info)
#             self.work += 1

# class Pupil:
#     def init(self):
#         self.knowledge = []

#     def take(self, info):
#         self.knowledge.append(info)

# lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')

# marivanna = Teacher()
# valya = Pupil()
# petya = Pupil()

# marivanna.teach(lesson[3], valya, petya)
# marivanna.teach(lesson[0], petya)

# print(valya.knowledge)
# print(petya.knowledge)


# class NewClass:
#     def init(self, x):
#         self.x = x
#     # def str(self):
#     #     return f'Значение объекта NewClass = {self.x}'
#     def repr(self):
#         return f'NewClass: {self.x}'
# a = NewClass(123)
# print(a)
# b = NewClass('Hello, World!')
# print(b)
