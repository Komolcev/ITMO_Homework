# SQL:

# select book_author, book_title, price,
# case
# 	when price > 150 then 'Very good'
# 	when price < 200 then 'So So'
# 	when price = 100 then 'Optimal'
# 	else 'OK!'
# end as comment

# select * from test where book_author in ('Лев Толстой', 'Пушкин')
# select * from test where book_title like '% и $'
# select * from test where book_title like '______%'
# select book_author, SUM(amount) from test group by book_author
# select count(amount) from test group by book_author


# insert into test values
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
# select * from test

# select book_author, min(price) as min_price from test group by author
# select author
# min (price) as Минимальная_цена,
# max (price) as Максимальная_цена,
# round (avg (price),2) as Средняя_цена
# from test


# select sum (amount) as Количество from test,
# select
# sum amount) as Количество,
# sum (price * amount) as Стоимость,
# Стоимость/Количество
# from book

# select book_title, book_author
# from test
# where price =
# (SELECT MIN(price) from test);
# Select book_title, amount, book_author
# from test
# where abs (amount - ...)


# select book_title, amount, price
# from test
# where book_author in (
# select book_author
# from test
# group by book_author
# having sum(amount) >= 12);


# CREATE table supply
# (supply_id int primary key,
# title text
# author text
# price int
# amount int)
# insert into book2 (title book_author, price, amount) values
# ('Над пропостью во ржи', 'Селинджер', 100, 5),
# ('Аэропорт', 'Хейли', 50, 20)


# create table author
# select *

# Команда которая должна сработать но я не вбивал:

# author_id int primary Key
# name_author varchar(50)
# create table author
# (author_id int primary key)
# name_author varchar(50))
# insert intoo author
# values
# (1, 'Буглаков М.А.')
# (2, 'Достоевский Ф.М.')
# (3, 'Есенин С.А.')
# (4, 'Пастернак Б.Л.')


# Команда INNER JOIN в SQL используется для объединения двух или более таблиц на основе совпадения значений указанных столбцов. Она возвращает только строки, имеющие соответствующие значения в обеих таблицах.

# Синтаксис команды INNER JOIN:

# SELECT *
# FROM таблица1
# INNER JOIN таблица2
# ON таблица1.столбец = таблица2.столбец;

# где:
# - таблица1 и таблица2 - имена таблиц, которые нужно объединить
# - столбец - общий столбец в таблицах, по которому нужно совместить их строки


# select * from test
# alter table test add column author_id int
# update test set author_id = 5 where book_author like 'Л%'
# select * from test


# select book.title, book.author
# from book_author inner join book2
# on author1.author_id = book2.author_id


# select book.title, book.author
# from book_author right join book2
# on author1.author_id = book2.author_id

# left join важнее. Если даже нет значения, то все равно выведет, а значение бдет null

# ! Вывод данных с SQL:

import psycopg2
con = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='4380',
    host='127.0.0.1',
    port='5433'
)

cur = con.cursor()
cur.execute
cur.execute('Select * from book order by title')
# cur.execute('Select * from book order by book_id')
rows = cur.fetchall()
for row in rows:
    # print('id={}'.format(row[0]))
    # print('title={}'.format(row[1]))
    # print('author={}'.format(row[2]))
    # print(row[3:])
    print(row)
con.close


# Там в презентации много вещей еще есть. Ченки её, если надо с SQL работать.
# ! pg_isready - команда для MacOS, чтобы проверить работает ли сервер sql
