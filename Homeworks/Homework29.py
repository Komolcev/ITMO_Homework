# # 29-1:
# def find_unique_number(nums):
#     result = 0
#     for num in nums:
#         result ^= num  # Используем операцию XOR для поиска уникального числа
#     return result

# # Пример использования
# numbers = [1, 4, 2, 3, 2, 4, 6, 6, 1]
# unique_number = find_unique_number(numbers)
# print(f"Уникальное число: {unique_number}")


# # 29-2:
# import heapq

# def find_optimal_path(matrix, start, end):
#     if not matrix or not matrix[0]:
#         return None

#     rows, cols = len(matrix), len(matrix[0])

#     # Создаем матрицу для хранения сумм путей
#     dp = [[float('inf')] * cols for _ in range(rows)]

#     # Очередь с приоритетами для хранения состояний (расстояния, координаты)
#     pq = [(0, start)]

#     while pq:
#         distance, current = heapq.heappop(pq)
#         i, j = current

#         # Если мы достигли конечной точки, возвращаем сумму пути
#         if current == end:
#             return distance + matrix[i][j]

#         # Проверяем все возможные направления
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         for di, dj in directions:
#             ni, nj = i + di, j + dj

#             # Проверяем, не выходит ли следующая клетка за границы матрицы
#             if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] >= 0:
#                 new_distance = distance + matrix[ni][nj]

#                 # Если новый путь короче, обновляем значение и добавляем в очередь
#                 if new_distance < dp[ni][nj]:
#                     dp[ni][nj] = new_distance
#                     heapq.heappush(pq, (new_distance, (ni, nj)))

#     # Если конечная точка недостижима
#     return None

# # Пример использования
# matrix = [
#     [1, 2, 3],
#     [4, -1, 6],
#     [7, 8, 9]
# ]

# start_point = (0, 0)
# end_point = (2, 2)

# result = find_optimal_path(matrix, start_point, end_point)
# print(f"Оптимальная сумма пути: {result}")


# # 29-3:
# def is_isomorphic(word1, word2):
#     if len(word1) != len(word2):
#         return False

#     mapping = {}
#     used_letters = set()

#     for char1, char2 in zip(word1, word2):
#         if char1 in mapping:
#             if mapping[char1] != char2:
#                 return False
#         else:
#             if char2 in used_letters:
#                 return False
#             mapping[char1] = char2
#             used_letters.add(char2)

#     return True


# # Пример использования
# print(is_isomorphic("CBAABC", "DEFFED"))  # True
# print(is_isomorphic("XXX", "YYY"))        # True
# print(is_isomorphic("RAMBUNCTIOUSLY", "THERMODYNAMICS"))  # True
# print(is_isomorphic("MAMA", "PAPA"))  # True

# print(is_isomorphic("AB", "CC"))  # False
# print(is_isomorphic("XXY", "XYY"))  # False
# print(is_isomorphic("ABAB", "CD"))  # False
