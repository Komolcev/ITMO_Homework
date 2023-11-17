import math as m
import pandas as pd
import numpy as np
import matplotlib as plt


# Общий родитель:
class food:
    def init(self, name, calories):
        self.name = name
        self.calories = calories


# Гарнир:
class side_dish(food):
    pass

# Мясо:


class meat(food):
    pass

# Напиток:


class drink(food):
    pass


# на 100 грамм или 100 мл:
side_dish = [
    side_dish('Гречка', 108),
    side_dish('Рис', 116),
    side_dish('Макароны', 157),
    side_dish('Пюре', 106)
]

meat = [
    meat('Домашняя котлета', 222),
    meat('Котлета пожарская', 231),
    meat('Курица вареная', 170),
    meat('Печеночная котлета', 164)
]

drink = [
    drink('Чай черный с молоком и с сахаром', 50),
    drink('Кока-кола', 42),
    drink('Сок', 47),
    drink('Молоко', 60)
]
