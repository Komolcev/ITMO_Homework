# # Питон запоминает что ты в него положил
# def add_fruit(fruit, basket=[]):
#     basket.append(fruit)
#     return basket
# b = add_fruit('Banana')
# print(b)
# c = add_fruit('Apple')
# print(c)
# d = add_fruit('Orange')
# print(d)

# ! OR

# def add_fruit(fruit, basket = None):
#     if basket == None:
#         basket = []
#     basket.append(fruit)
#     return basket
# b = add_fruit('Banana')
# print(b)
# c = add_fruit('Apple')
# print(c)
# d = add_fruit('Orange')
# print(d)


# class SomeClass:
#     def _init__(self): pass
#     def __call__(self, x, y): return x/y
#     def __getitem__(self, i): return i*i
# a = SomeClass()
# # print(a(40, 4))
# print(a[5])


# class Student:
#     stdnt = []

#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
#         self.summa = self.fives*5 + self.tens*10 + self.twenties*20
#         Student.stdnt.append(self)

#     def result(self):
#         for i in Student.stdnt:
#             print(i.name, i.summa)


# a = Student('Oleg', 1, 1, 1)
# b = Student('Ivan', 2, 2, 2)
# c = Student('Petya', 0, 2, 5)

# a.result()


# class SomeClass:
#     def __init__(self, x):
#         self.__age = 42
#         self.x = x
#         self._spisok = []

# obj = SomeClass(10)
# obj._spisok.append(123)
# print(obj.__dict__)
# print(obj.__dir__())


# __ 2 лучше не передавать никуда информацию, закрытый элемент
# _ 1 на усмотрение программиста


# class Person(object):
#     instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#         return cls.instance
#     def __init__(self):
#         self.__name = 'Peter I'
# obj_one = Person()
# obj_two = Person()
# print(obj_one is obj_two)


# class Student:
#     stdnt = []

#     def __init__(self, name, fi, te, tw):
#         self.name = name
#         self.fi = fi
#         self.te = te
#         self.tw = tw
#         self.su = self.fi*5 + self.te*10 + self.tw*20
#         Student.stdnt.append(self)

#     def result(self):
#         results = []
#         for st in Student.stdnt:
#             results.append(f"{st.name}: {st.su}")
#         return "\n".join(results)


# a = Student('Иванов', 1, 1, 1)
# b = Student('Петров', 2, 2, 2)
# c = Student('Сидоров', 3, 3, 3)
# print(a.result())


# class Car:
#     def __init__(self, model, color, vin, horse_pover):
#         self.model = model
#         self.color = color
#         self.VIN = vin
#         self.horse_pover = horse_pover

#     def __repr__(self):
#         return f'{self.model} {self.color} {self.VIN} {self.horse_pover}'

#     def __str__(self):
#         return f'My Favorite Car: {self.VIN} {self.color} {self.model} {self.horse_pover}'


# lada = Car('Сhevrolet Niva', 'Dark Blue', 'О620ВН11', '80')
# BMW = Car('BMW', 'Black', 'O333OO190', '350')
# lada.price = 2000000
# # print(str(lada))
# lada.color = 'Purple'
# print(lada.__dict__) # Изменяет объект прямо на ходу!
# print(BMW)


# class A:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z


#     def __str__(self):
#         lst = []
#         for k, v in self.__dict__.items():
#             lst.append(f'{k}:{v}')
#         print(lst)
#         return ','.join(lst[::-1])

# a = A(1, 2, 3)
# a.abcd = 'abcd'
# a.w = 123
# print(a)


# # Вторая программа модуль __eq__
# class Car:
#     def __init__(self, model, color, vin):
#         self.model = model
#         self.color = color
#         self.vin = vin
#     def __eq__(self, other):
#         return self.vin == other.vin
#     def __str__(self):
#         return f'Автомобиль: {self.model} {self.color} {self.VIN}'

# lada = Car('Lada', 'Red', '12345')
# BMW = Car('BMW', 'Black', '43210')

# print(BMW == lada)


# class B:
#     def __init__(self, x):
#         self.x = x
#     def __eq__(self, other):
#         return bool (1-(self.x + other.x) % 2)
# b1 = B(1)
# b2 = B(2)
# print(b1 == b2)

# # Есть еще оператор больше: __gt__
# # __lt__ - сравнение


class Factorial:
    def __init__(self):
        self.value = 1
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.value *= self.index
        self.index += 1
        return self.value


f = Factorial()
for i in range(10):
    print(next(f), f.value, f.index)
