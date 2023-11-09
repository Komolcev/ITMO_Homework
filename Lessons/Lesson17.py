# # "Я кортеж, кортеж менять нельзя, но ладно"
# # То есть можно загасить трай эксепт
# some_tuple = ([1,2], [3,4], [5,6,7,8])
# try:
#     some_tuple[2] += [7,8]
# except TypeError:
#     print(some_tuple)
# # # Взял, изменил все равно (и снизу тоже)
# # some_tuple[2].append([7,8])
# # print(some_tuple)


# import re
# print(re.findall(r'<.*>', '<f> <s> <t>')) # Жадный поиск
# print(re.findall(r'<.*?>', '<f> <s> <t>')) # Ленивый поиск


# # ДЗ 16-1:
# import re
# re.sub(r'\b\w+\b', lambda x:x.group().title()[0], input()) # .replace(' ', '')


# # ДЗ 16-2:
# import re
# n = int(input('--->'))
# x, y = divmod(n, 10) # * Замена // и %
# # print(n,x,y)
# r = []
# r.append(r'\b\d\b') # от 0 до 9
# r.append(r'\b10\b') # 10
# if n == 10:
#     regex = '|'.join(r[:2])
# elif n < 20:
#     r.append(rf'\b1[0-{y}]\b') # от 10 до 19
#     regex = '|'.join(r[:3])
# else:
#     r.append(rf'\b[1-{x-1}]\d\b') # от 10 до 39
#     r.append(rf'\b{x}[0-{y}]\b') # от 40 до 45
#     regex = '|'.join(r[:4])
# print(*re.findall(regex, str(list(range(200)))))


# В две строчки то же самое что и сверху:
# pattern = rf"\s[0-{a//10}][0-{a%10}]?\b|\s[0-{(a//10)-1}]?\d\b"
# print(', '.join([i.strip() for i in re.findall(rf"{pattern}", text)]))


# import re
# text = 'Миша:123 Коля:234 Сеня:345'
# res = re.findall(r'(\w+):(\d+)', text)
# print(res)


# import re
# text = 'abracadabra'
# res = re.finditer(r'abrac', text)
# for i in res:
#     print(i.group(), i.start(), i.end())


# import re
# numbers = re.compile(r'\d+')
# print(re.findall(numbers, 'Я живу в доме 5'))
# print(numbers.findall('Прочитайте абзац 8 на странице 10'))


# import re
# def podslovo(text, os):
#     return re.findall(rf'\b\w+{os}\w*\b', text)
# text = 'Косой косой косил волос на осине'
# os = 'ос'
# print(podslovo(text, os))


# def sample_decorator(func):
#     def wrapper():
#         print('Начало')
#         func()
#         print('Конец')
#     return wrapper
# def say():
#     print('Привет МИР!')
# say = sample_decorator(say)
# @sample_decorator
# def buy():
#     print("BYE!")
# buy()


# def deco(func):
#     def wrapper(*args, **kwargs):
#         # 1
#         # args kwargs
#         value = func(*args, **kwargs)
#         # 2
#         # args kwargs
#         # value
#         return value
#     return wrapper


# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         val = func(*args,**kwargs)
#         end = time.perf_counter()
#         work_time = end - start
#         print(f'Время выполнения {func.__name__}:{round(work_time, 4)} сек')
#         return val
#     return wrapper

# @timer
# def test(n):
#     return sum([(i/99)**2 for i in range(n)])

# @timer
# def sleep(n):
#     time.sleep(n)

# res1 = test(10000)
# res2 = sleep(4)
# print(f'Результат функции test = {res1}')
# print(f'Результат функции sleep = {res2}')


# # Журналирвоание
# import time
# def clue(func):
#     def wrapper(*args, **kwargs):
#         with open('log.txt', 'w') as f:
#             print(time.time(), 'start', {func.__name__}, file=f)
#         val = func(*args, **kwargs)
#         with open('log.txt', 'w') as f:
#             print(time.time(), 'end', {func.__name__}, file=f)
#         res = ''
#         for i in args:
#             res += i
#         return res
#     return wrapper
# @clue
# def test(*args): return None
# print(test('aaa', 'bbb', 'ccc'))
# print(test('a', 'b', 'c', 'd', 'e'))
# @clue
# def comp_str(x, y):
#     return x > y
# print(comp_str('a', 'b'))


# *ООП:
# В Python все объекты какого то класса
# ООП: класс, объекты (инстансы), функции = методы, атрибуты, наследование ...
# Класс это тоже тип данных
# объект, экземпляр, инстанс одно и то же


class Person:

    # Два подчерка это ДАНДА - дабл андерскоо - фунция для создания объекта
    def __init__(self, name, money, age):
        self.name = name  # селф используется при создании объекта
        self.money = money
        self.age = age  # Эта штука прописывается для всех

# a = Person('Pete', 200)
# b = Person('Nick', 300)
# a.age = 99 # Меняем аргумент для одного конкретного объекта
# print(a.name, a.money, a.age)
# print(b.name, b.money, b.age)
# print(b.name, b.money, a.age) # тут вставили age с другого объекта

#     def give_money(self, other, x):
#         if x <= self.money:
#             other.money += x
#             self.money -= x
#         else:
#             print(
#                 'Маме сделал подарок сегодня на д.р. духи и осталось 0 рублей у меня :( ')

#     # def info(self):
#         # print(f'{self.name}, {self.money}, {self.age}')

#     def socialism(self, other):
#         total = self.money + other.money
#         self.money = total / 2
#         other.money = total / 2


# a = Person('Pete', 200, 99)
# b = Person('Nick', 300, 55)
# a.give_money(b, 100)
# print(a.money, b.money)
# # a.socialism(b)
# # b.socialism(a)
# b.give_money(a, 200)
# # a.info()
# # b.info()
# print(a.money, b.money)


# Женя написала:
# def soc(self, other):
#     if self.money != other.money:
#         dif = abs(self.money - other.money) // 2
#         if self.money < other.money:
#             self.money += dif
#             other.money -= dif
#         else:
#             self.money -= dif
#             other.money += dif
