# 21-1:
# ID ученика (pupil_ID)
# Имя (first_name)
# Фамилия (family_name)
# Отчество (last_name)
# Дата рождения (date_of_birth)
# Пол (sex)
# Адрес электронной почты (e-mail)
# Номер телефона (phone_number)
# Город (city)
# Страна (country)
# Университет (unversity)
# Специальность (occupation)
# Дата начала обучения (enrollment_date)
# Дата окончания обучения (graduation_date)
# Преподаватель (teacher)
# Оплата (payment)


# 21-2:
# Рандомный размер матрицы и числа в ней (до 30)
import random


def shortest_path(matrix, x, y):
    if x == 0 and y == 0:
        return [matrix[0][0]], matrix[0][0]
    elif x == 0:
        path, total = shortest_path(matrix, x, y-1)
        path.append(matrix[x][y])
        return path, total + matrix[x][y]
    elif y == 0:
        path, total = shortest_path(matrix, x-1, y)
        path.append(matrix[x][y])
        return path, total + matrix[x][y]
    else:
        path1, total1 = shortest_path(matrix, x-1, y)
        path2, total2 = shortest_path(matrix, x, y-1)
        if total1 <= total2:
            path1.append(matrix[x][y])
            return path1, total1 + matrix[x][y]
        else:
            path2.append(matrix[x][y])
            return path2, total2 + matrix[x][y]


# Создание рандомной матрицы
n = random.randint(2, 8)
matrix = [[random.randint(1, 30) for _ in range(n)] for _ in range(n)]

# Поиск самого короткого пути и его суммы
path, total = shortest_path(matrix, n-1, n-1)

# Вывод результатов
print("Матрица:")
for row in matrix:
    print(row)

print("\nСамый короткий путь:")
print(" -> ".join(str(x) for x in path), "=", total)


# 21-3:
# create table book (book_id int, book_title text, book_author text, publisher_id int, pages int)
# insert into book values
# (1, 'Война и мир', 'Лев Толстой', 100, 1225),
# (2, 'Мастер и Маргарита', 'Михаил Булгаков', 101, 462),
# (3, 'Гордость и предубеждение', 'Джейн Остин', 102, 432),
# (4, 'Преступление и наказание', 'Федор Достоевский', 100, 592),
# (5, 'Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', 101, 180)
# (6, 'Тихий Дон', 'Михаил Шолохов', 102, 864)
# (7, 'Алиса в Зазеркалье', 'Льюис Кэрролл', 100, 272)
# (8, 'Властелин колец: Братство кольца', 'Дж. Р. Р. Толкин', 101, 432)
# (9, 'О дивный новый мир', 'Олдос Хаксли', 102, 288)
# (10, 'Анна Каренина', 'Лев Толстой', 100, 864)
# (11, 'Фауст', 'Иоганн Вольфганг фон Гёте', 101, 448)
# (12, 'Мертвые души', 'Николай Гоголь', 102, 352)
# (13, 'Одноэтажная Америка', 'Ильф и Петров', 103, 240)
# (14, 'Портрет Дориана Грея', 'Оскар Уайльд', 104, 254)
# (15, 'Братья Карамазовы', 'Федор Достоевский', 105, 824)
# select * from book
# select book_title from book where publisher_id = 100
# select book_title from book where publisher_id = 103 # 1 результат
# select * from book where pages like '4%' # 4 результата
