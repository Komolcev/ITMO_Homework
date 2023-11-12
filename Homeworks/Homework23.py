# # 23-1:
# import psycopg2
# import pandas as pd

# def longest_palindrome(s):
#     n = len(s)
#     m = [[0] * n for _ in range(n)]

#     for i in range(n):
#         m[i][i] = 1

#     max_length = 1

#     for cl in range(2, n + 1):
#         for i in range(n - cl + 1):
#             j = i + cl - 1
#             if s[i] == s[j] and cl == 2:
#                 m[i][j] = 2
#             elif s[i] == s[j]:
#                 m[i][j] = m[i + 1][j - 1] + 2
#             else:
#                 m[i][j] = max(m[i][j - 1], m[i + 1][j])
#             max_length = max(max_length, m[i][j])
#     return max_length

# input_str = 'aaabaaac'
# result = longest_palindrome(input_str)
# print(f"Длина наибольшей подстроки-палиндрома: {result}")


# # 23-2:
# # Эта часть должна быть в pgAdmin 4:
# create table test (book_id int, title text, author text, publisher_id int, pages int, price int, amount int, total int)
# insert into test values
# (1, 'Война и мир', 'Лев Толстой', 100, 1225, 600, 12),
# (2, 'Мастер и Маргарита', 'Михаил Булгаков', 101, 462, 800, 20),
# (3, 'Гордость и предубеждение', 'Джейн Остин', 102, 432, 300, 15),
# (4, 'Преступление и наказание', 'Федор Достоевский', 100, 592, 400, 20),
# (5, 'Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', 101, 180, 350, 32),
# (6, 'Тихий Дон', 'Михаил Шолохов', 102, 864, 100, 100),
# (7, 'Алиса в Зазеркалье', 'Льюис Кэрролл', 100, 272, 200, 61),
# (8, 'Властелин колец: Братство кольца', 'Дж. Р. Р. Толкин', 101, 432, 250, 30),
# (9, 'О дивный новый мир', 'Олдос Хаксли', 102, 288, 400, 90),
# (10, 'Анна Каренина', 'Лев Толстой', 100, 864, 60, 120),
# (11, 'Фауст', 'Иоганн Вольфганг фон Гёте', 101, 448, 80, 1000),
# (12, 'Мертвые души', 'Николай Гоголь', 102, 352, 25, 55),
# (13, 'Одноэтажная Америка', 'Ильф и Петров', 103, 240, 12, 12),
# (14, 'Портрет Дориана Грея', 'Оскар Уайльд', 104, 254, 100, 20),
# (15, 'Братья Карамазовы', 'Федор Достоевский', 105, 824, 20, 100)
# select * from test
# UPDATE test
# SET total = price * amount


# # Эту часть надо выполнить в Питоне:
# # Подключение к локальному серверу на компьютере:
# conn = psycopg2.connect(
#     database='postgres',
#     user='postgres',
#     password='4380',
#     host='127.0.0.1',
#     port='5433'
# )
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM test")

# # Получение результатов запроса в виде списка кортежей
# results = cursor.fetchall()

# # Закрытие подключения
# cursor.close()
# conn.close()

# # Создание и вывод DataFrame
# df = pd.DataFrame(results, columns=[
#                   '№', 'Заголовок', 'Автор', 'Издание', 'Страницы', 'Цена', 'Кол-во', 'Всего'])
# print(df)


# # 23-3:
from functools import cmp_to_key


def largest_number(nums):
    def compare(x, y):
        return int(x + y) - int(y + x)

    sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)

    result = ''.join(sorted_nums)

    return result


input1 = [32, 3, 45]
result1 = largest_number(input1)
print(f"Для входа {input1}, результат: {result1}")
