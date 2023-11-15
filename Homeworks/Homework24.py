# # 24-1:
# a = [17, 67, 58, -3, -71, -17, 82, 0, -97, 47, -86, 100, -30, 93, 97, -47, -78, -24, 11, -19, 21, -66, 69, -55, -62]
# n = len(a)
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)


# # 24-2:
# CREATE TABLE Task24_2 (book_id int, book_title text, book_author text, publisher_id int, price int, count int)
# insert into Task24_2 values
# (1, 'Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', 100, 256),
# (2, 'Мастер и Маргарита', 'Михаил Булгаков', 101, 448),
# (13, 'Собачье сердце', 'Михаил Булгаков', 101, 243),
# (13, 'Морфий', 'Михаил Булгаков', 101, 332),
# (3, '1984', 'Джордж Оруэлл', 100, 328),
# (14, 'Скотный двор', 'Джордж Оруэлл', 100, 289),
# (4, 'Тысяча великих солнц', 'Халед Хоссейни', 100, 384),
# (5, 'Гарри Поттер и философский камень', 'Дж. К. Роулинг', 101, 320),
# (10, 'Мартин Иден', 'Джек Лондон', 100, 448),
# (11, 'Фауст', 'Иоганн Вольфганг фон Гёте', 100, 448),
# (12, 'Гарри Поттер и Дары Смерти', 'Дж. К. Роулинг', 100, 784)

# CREATE VIEW author_books_count AS
# SELECT book_author, COUNT(*) AS books_count
# FROM Task24_2
# GROUP BY book_author;
# select * from author_books_count

# SELECT abc.book_author, abc.books_count
# FROM author_books_count abc
# WHERE abc.books_count = (SELECT MIN(books_count) FROM author_books_count);


# # 24-3:
# def count_skb(s):
#     stack = []
#     for char in s:
#         if char == '(':
#             stack.append('(')
#         elif char == ')':
#             if not stack:
#                 return False
#             stack.pop()
#     return not stack

# print(count_skb("()"))
# print(count_skb(")(((()))"))
# print(count_skb("("))
# print(count_skb("(()) (( () () ) () )"))
# print(count_skb("(()"))
