# # 23-1:
def longest_palindrome_substring(s):
    # Создаем таблицу размером NxN, где N - длина строки s
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # Разные начала
    max_length = 1
    start = 0
    for i in range(n):
        dp[i][i] = True

    # Проверяем все пары символов в строке
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max_length = 2
            start = i

    # Проверяем все подстроки длины более 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                max_length = length
                start = i

    # Возвращаем самую длинную палиндромную подстроку
    return s[start:start+max_length]


s = input("Введите строку: ")
longest_palindrome = longest_palindrome_substring(s)
print("Самая длинная палиндромная подстрока:", longest_palindrome)


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
#     password=
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
# from functools import cmp_to_key


# def largest_number(nums):
#     def compare(x, y):
#         return int(x + y) - int(y + x)

#     sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)

#     result = ''.join(sorted_nums)

#     return result


# input1 = [32, 3, 45]
# result1 = largest_number(input1)
# print(f"Для входа {input1}, результат: {result1}")
