# class A:
#     def __init__(self, limit):
#         self.limit = limit

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.limit <= 0:
#             raise StopIteration
#         else:
#             self.limit -= 1
#             return self.limit


# b = A(5)
# for i in b:
#     print(111, i)
#     # print(222,  next(b))
#     # print(333,  next(b))


# * StopIteration выскочил потому, что next явный
# * Блок-схемы включены иногда в документацию (на уровне подсистем)
# * Swim-lane диаграмы тоже хорошие и интересные, подобие блок-схем (+ там добавляется ответственность)
# * Business Process Model and Notation (BPMN) - то же самое
# * Use-case диаграммы - кто кому дает задачи, кто за что отвечает
# * EPC (Event-driven Process Chain) диаграммы - сочитает в себе все + в цветах, в каком виде кто кому отчитывается, во главе угла - событие (самое универсальное средство)
# * Бизнес-аналитик расспрашивает заказчика и фиксирует все процессы сначала на бумагу, а потом уже все это переносится на задачи программистам
# * matplotlib - мощная рисовалка


# import numpy as np
# a = np.array([1,2,3])
# b = np.array([2,2,2])
# c = a >= b
# print(a[c])
# # pandas лучший инструмент для анализа данных. Он может справится с данными, которые даже до конца не заполнены


# import pandas as pd
# import random
# df = pd.DataFrame(columns=['Год', 'Товар', 'Штук', 'Цена'],
#                   index=range(20))
# x = 0
# for i in range(2001, 2006):
#     for j in ['A', 'B', 'C', 'D']:
#         k = [10, 20, 30, 40, 50][random.randint(0, 4)]
#         m = [100, 50, 30, 20, 5][random.randint(0, 4)]
#         df.iloc[x] = [i, j, k, m]
#         x += 1
# df['Итого'] = df['Цена'] * df['Штук']
# df1 = df


# print(df)
# print(df1['Итого'])
# print(df1[['Цена', 'Итого']])
# print(df1.loc[0:0])
# print(df1.head(6))
# print(df1[df1.Итого > 2000])
# print(df1['Итого'])
# print(df1.iloc[0])
# df2 = df1.tail()
# df2.loc[16]
# print(df1.tail())


# iloc = по номеру
# loc = по значению индекса


# print(df.loc[0,'Итого'])
# print(df.columns) # Какие колонки
# print(df1.index) # Какие индексы


# Добавить год:
# df1.loc[20] = [2019, 'E', 10, 20, 200]


# print(df1)
# print(len(df1['Товар'].unique()))
# print(len(df1[df1['Итого'] > 1500])) # Позиций больше чем 1500
# print(df1.Итого.sum())
# print(df1.describe)
# maxx = df1.Итого.max()
# print(maxx)
# df1[df1.Итого == df1.Итого.max()]
# print(df1[0:len(df1)])
# me = df1.Цена.mean()
# print(me)
# print(df.sort_values('Итого').head(3))
# print(df1.groupby('Товар').Итого.sum())


# ! СУБД:
# create table book3 (id int, author text, name text);
# select * from book 3
#  ! Надо выделять строчку и потом ее запускать
#  ! Только такие ковычки "" использовать
#  ! Правой кнопкой мыши в pgAdmin4 -> View/Edit Data -> All Rows
# insert into book3 values
# (1, 'Пушкин', 'Евгений Онегин')
# (2, 'Лермонтов', 'Герой Нашего Времени')
# (3, 'Пушкин', 'Капитанская дочка')
# (4, 'Толстой', 'Война и мир')
# select * from book3 where author = 'Пушкин'
# select * from book3 where name like "B%"
