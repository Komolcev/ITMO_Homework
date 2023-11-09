# #20-1:
# #Ради интереса запихнул метод рандом (который относится и к покупателям и к товарам),
# #можно было и прописать покупателей и что они покупают
# import random

# class Visitor:
#     def __init__(self, name):
#         self.name = name

#     def order_drink(self, drink):
#         return f"{self.name} заказал {drink.name}"

#     def order_cake(self, cake):
#         return f"{self.name} заказал {cake.name}"


# class Drink:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class Cake:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# drinks = [
#     Drink("Черный чай", 10),
#     Drink("Зеленый чай", 11),
#     Drink("Латте", 15),
#     Drink("Капучино", 14),
#     Drink("Американо", 17),
#     Drink("Лимонад", 13),
#     Drink("Кола", 12),
#     Drink("Пиво", 17)
# ]

# cakes = [
#     Cake("Торт", 20),
#     Cake("Пирог с мясом", 21),
#     Cake("Эклер", 19),
#     Cake("Печенье", 14),
#     Cake("Булка", 13),
#     Cake("Пирог с творогом", 15),
#     Cake("Шоколадка", 19)
# ]

# def generate_random_order():
#     order = ""
#     number_of_items = random.randint(1, 4)
#     for _ in range(number_of_items):
#         if random.choice([True, False]):
#             item = random.choice(drinks)
#             order += f"{item.name} - {item.price} руб.\n"
#         else:
#             item = random.choice(cakes)
#             order += f"{item.name} - {item.price} руб.\n"
#     return order


# def generate_random_visitors():
#     number_of_visitors = random.randint(1, 11)
#     visitors = []

#     for i in range(number_of_visitors):
#         visitor = Visitor(f"Посетитель {i+1}")
#         visitors.append(visitor)
#     return visitors

# daily_profit = 0

# visitors = generate_random_visitors()
# for visitor in visitors:
#     order = generate_random_order()
#     print(f"{visitor.name}:\n{order}")
#     items = order.split("\n")[:-1]
#     for item in items:
#         item_name, item_price = item.split(" - ")
#         item_price = int(item_price[:-4])
#         daily_profit += item_price

# print(f"Прибыль за день: {daily_profit} руб.")


# # 20-2:
# # Не совсем понял то, куда правильно запихнуть общую сумму, поэтому решил реализовать её прямо в таблицу для красоты
# import pandas as pd
# import numpy as np

# def sum_all_numbers(df):
#     numbers_df = df.select_dtypes(include='number')
#     total_sum = (numbers_df.iloc[:, -1] * numbers_df.iloc[:, -2]).values.sum()
#     return total_sum

# dct = {'Товар:': ['Молоко', 'Хлеб', 'Сахар', 'Мясо', 'Масло', 'Курица'],
#        'Цена:': [50, 35, 30, 65, 40, 20],
#        'Количество:': [2, 3, 2, 3, 1, 5]}
# df1 = pd.DataFrame(dct)
# df1['Цена:'] = pd.to_numeric(df1['Цена:'])
# df1['Количество:'] = pd.to_numeric(df1['Количество:'])
# df1['Итог:'] = df1['Количество:'] * df1['Цена:']

# total_sum_np = np.sum(df1['Итог:'].values)

# result1 = sum_all_numbers(df1)

# df1 = df1._append({'Товар:': 'ВСЕГО:', 'Цена:': '', 'Количество:': '', 'Итог:': total_sum_np}, ignore_index=True)

# print(result1)
# print(df1)
# df1['Итог:'].plot(kind='barh')


# 20-3:
import itertools

n = int(input('Введите количество необходимых комбинаций: '))


class InfiniteSequence:
    def __init__(self):
        self.seq = itertools.count(1)
        self.letters = itertools.cycle('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def get_next(self):
        number = next(self.seq)
        if number > 26:
            self.seq = itertools.count(1)
            next(self.letters)
        return str(number) + ' ' + next(self.letters)


sequence = InfiniteSequence()
for i in range(n):
    print(sequence.get_next(), end=' ')
