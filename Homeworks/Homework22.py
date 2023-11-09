# 22-1:
# create table test2 (book_id int, book_title text, book_author text, publisher_id int, pages int)
# insert into test2 values
# (1, 'Война и мир', 'Лев Толстой', 100, 1225),
# (2, 'Мастер и Маргарита', 'Михаил Булгаков', 101, 462),
# (3, 'Гордость и предубеждение', 'Джейн Остин', 102, 432),
# (4, 'Преступление и наказание', 'Федор Достоевский', 100, 592),
# (5, 'Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', 101, 180),
# (6, 'Тихий Дон', 'Михаил Шолохов', 102, 864),
# (7, 'Алиса в Зазеркалье', 'Льюис Кэрролл', 100, 272),
# (8, 'Властелин колец: Братство кольца', 'Дж. Р. Р. Толкин', 101, 432),
# (9, 'О дивный новый мир', 'Олдос Хаксли', 102, 288),
# (10, 'Анна Каренина', 'Лев Толстой', 100, 864),
# (11, 'Фауст', 'Иоганн Вольфганг фон Гёте', 101, 448),
# (12, 'Мертвые души', 'Николай Гоголь', 102, 352),
# (13, 'Одноэтажная Америка', 'Ильф и Петров', 103, 240),
# (14, 'Портрет Дориана Грея', 'Оскар Уайльд', 104, 254),
# (15, 'Братья Карамазовы', 'Федор Достоевский', 105, 824)
# select * from test2
# SELECT book_title, book_author FROM test2 ORDER BY book_author ASC;
# SELECT book_title, book_author FROM test2 ORDER BY book_title DESC;


# 22-2:
# def find_max_length(graph, start, end):

#     # Создание графа
#     adjacency_list = {}
#     for edge in graph:
#         a, b = edge
#         if a not in adjacency_list:
#             adjacency_list[a] = []
#         adjacency_list[a].append(b)

#     # Функция поиска в глубину
#     def dfs(current_node, path_length, max_length):
#         if current_node == end:
#             max_length = max(path_length, max_length)
#         if current_node in adjacency_list:
#             for next_node in adjacency_list[current_node]:
#                 max_length = dfs(next_node, path_length + 1, max_length)
#         return max_length
#     return dfs(start, 0, 0)

# graph = [(1,2),(1,3),(2,4),(2,5),(3,6),(6,7),(7,8)]
# start_node = 1
# end_node = 8

# max_length = find_max_length(graph, start_node, end_node)
# print("Максимальная длина:", max_length)


# 22-3:
import keyword
kwlist = keyword.kwlist

s = "Если я пойду False и долиною and смертной None тени, не убоюсь True зла, потому as что Ты for со мной; Твой жезл и if Твой посох — они global успокаивают меня. Ты приготовил or предо мною try трапезу в виду while врагов моих; умастил елеем lambda голову мою; чаша моя del преисполнена.".split()
for i in range(len(s)):
    if s[i] in kwlist:
        s[i] = '<kw>'

print(*s)
