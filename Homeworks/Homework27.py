# # 27-1:
# def generate_darts_matrix(n):
#     if not (1 <= n <= 18):
#         print("Введите число n от 1 до 18.")
#         return

#     matrix = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(i, n - i):
#             matrix[i][j] = matrix[j][i] = matrix[n - i - 1][j] = matrix[j][n - i - 1] = min(i, j) + 1

#     for row in matrix:
#         print(" ".join(map(str, row)))


# n = int(input("Введите число n от 1 до 18: "))
# generate_darts_matrix(n)


# # 27-2:
# class Item:
#     def __init__(self, name, price, quantity):
#         self._name = name
#         self._price = price
#         self._quantity = quantity

#     @property
#     def name(self):
#         return self._name.capitalize()

#     @property
#     def total(self):
#         return self._price * self._quantity


# item = Item("book", 10, 2)

# print(f"Название предмета: {item.name}")
# print(f"Общая стоимость: {item.total} рублей")


# # 27-3:
# def count_elements(lst):
#     count = 0

#     for item in lst:
#         count += 1
#         if isinstance(item, list):
#             count += count_elements(item)

#     return count

# example1 = [1, 1, [1, 1,[[[1]]]]]
# example2 = [1, 2, 3]
# example3 = ["x", "y", ["z"]]
# example4 = [1, 2, [3, 4, [5]]]

# print(count_elements(example1))
# print(count_elements(example2))
# print(count_elements(example3))
# print(count_elements(example4))
