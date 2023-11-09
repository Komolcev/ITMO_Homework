import pandas as pd

# a = {'Год':[2001, 2002, 2003, 2004], 'Шт':[1,2,3,4], 'А':[100,200,300,400]}
# df = pd.DataFrame(a, index = [2001,2002,2003,2004])
# df1 = pd.DataFrame({'Company':['aa', 'bb', 'cc', 'dd', 'ee']}, index = [2001, 2002, 2003, 2004, 2005])
# df2 = df.join(df1)
# print(df2)


# a = {'Год':[2001, 2002, 2003, 2004], 'Шт':[1,2,3,4], 'А':[100,200,300,400]}
# df = pd.DataFrame(a, index = [2001,2002,2003,2004])
# df1 = df.loc[[2001,2002]]
# df2 = df.loc[[2003,2004]]
# print(df1)
# print(df2)
# df3 = pd.concat([df1, df2])
# print(df3)


# # * Визуализация
# import matplotlib.pyplot as plt
# df = pd.DataFrame({'a':[1,2,3,4,5,6,7,8,9],
#                    'b':[1,1,2,2,3,3,4,4,5],
#                    'c':[3,6,9,12,15,18,21,24,27]})
# df.index = df['a']
# df[['a','b','c']].plot()
# print(plt.show())
# # Есть еще гистограммы (вертикальне и горизонтальные)

# # * Распределение точек
# import matplotlib.pyplot as plt
# import random
# x,y = [],[]
# for _ in range(10):
#     x.append(random.random())
#     y.append(random.random())
# df = pd.DataFrame({'x':x,'y':y})
# df.plot('x','y', kind='scatter')
# print(plt.show())


# * DB
# select * from book2
# alter table book2 add column total int
# update book2 set total = price * amount

# * Ошибся в названиях, если что:
# create table book_hello (book_title text, book_author text, ptice int, amount int)
# insert into book_hello values
# ('Война и мир', 'Лев Толстой', 600, 12),
# ('Мастер и Маргарита', 'Михаил Булгаков', 700, 20),
# ('Гордость и предубеждение', 'Джейн Остин', 800, 43),
# ('Преступление и наказание', 'Федор Достоевский', 900, 54),
# ('Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', 1010, 56),
# ('Тихий Дон', 'Михаил Шолохов', 1020, 67),
# ('Алиса в Зазеркалье', 'Льюис Кэрролл', 1100, 87),
# ('Властелин колец: Братство кольца', 'Дж. Р. Р. Толкин', 100, 98),
# ('О дивный новый мир', 'Олдос Хаксли', 300, 100),
# ('Анна Каренина', 'Лев Толстой', 400, 120)
# select * from book_hello
# select book_title, amount from book_hello
# select book_title AS Название, amount as Количество from book_hello;
# select book_title, book_author, ptice, round(sqrt(amount)) from book_hello;
# select book_title, ptice from book_hello where ptice > 1
