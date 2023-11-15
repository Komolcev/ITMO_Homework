# print('7' < '71')
# select * from book2
# select * from author
# select name_author, title
# from book2 left join author
# on book2.author_id = author.author_id


# select * from book2
# select * from author
# select name_author, title
# from book2 full outer join author
# on book2.author_id = author.author_id


# select author_id, sum(amount) as sum_amount
# from book2 group by author_id


# select name_author, sum(amount) as Количество
# from author inner join book2
# on author.author_id = book2.author_id
# group by name_author
# having sum(amount) =
# select max(sum_amount) as max_sum_amount
# from
# (select author_id, sum(amount) as sum_amount
#  from book2 group by author_id) query_in


# select DISTINCT name_author
# from author inner join book2
# on author.author_id = book2.author_id
# where price =
# (select max(price) as max_price from book2)


# select * from book2 where price = 200
# # Первичный ключ (primary key) - называется атрибут или набор атрибутов, который уникальным образом идентифицирует сужность.
# # Если первичный ключ состоит более чем из одного атрибута, то его называют составным первичным ключем
# # Каждая сущность должна иметь первичный ключ, в противном случае вы никогда не сможете однозначно ее идентифицировать.
# # Требуется очен веские причины, почему ваша сущность не имеет первчного ключа, такое встречается, но крайне редко
# # Внешний ключ (foriegn key) - используются для организации связей между таблицами базы данных (родительскими и дочерними)
# # и для поддержания ограничений ссылочной целостности данных.


# select * from book2
# indert into book2 values (1001, '1','2',1,2,3,4)


# # Добавить связь между таблицами
# alter rable child_name
#     add constraint NAME_CONSTRAINT
#     foreign key(id_parent)
#     references parent_name(id_parent)
# # Связь один ко многим - в отделе может работать множество работников, но один работник работает в одном отделе
# # Связь многие ко многим - автор может написать множество книг, но одну книну может написать множество авторов
# # Связь один к одному


# # inner join
# # Шаблон запроса пересечения двух сущностей:
# select a.name, b.value
# from table1 a, table2 b
# where a.id = b.id


# select * from author1
# insert into author2 values
# (37, 'Солженицын')
# (38, 'Набоков')
# select * from author2


# select * from author1
# UNION ALL
# select * from author2


# select * from author1
# INTERSECT
# select * from author2


# create VIEW MAX_PRICE as
# (select author, sum(amount) from book2 group by author)

# select sum(amount), author from book2 group by author


# select * from MAX_PRICE order by author
# insert into book2 values (222, 'Солженицын', 'Архипелаг ГУЛАГ', 11, 22, 33, 44)
# select * from book2


# select author from MAX_PRICE
# WHERE sum = SELECT MAX(sum) FROM MAX_PRICE


# select sum(to_buy)
# from
# (
# select author, title, amount, 100 - amount as to_buy
# from book2
# where amount < 100
# order by to_buy
# ) qqq
