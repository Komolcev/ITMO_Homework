# # 28-1:
# def count_inversions(arr):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 count += 1
#     return count


# arr1 = [5, 3, 4, 3, 2]
# arr2 = [5, 4, 3, 2, 1]

# print(count_inversions(arr1))
# print(count_inversions(arr2))




# # 28-2:
# function = lambda s1, s2: sum(c1 != c2 for c1, c2 in zip(s1, s2))
# print(function("abc", "abc"))
# print(function("abc", "abd"))
# print(function("abc", "xyz"))




# # 28-3:
# def hanoi_moves(n):
#     if n == 1:
#         return 1
#     else:
#         return 2 * hanoi_moves(n - 1) + 1

# # Пример использования
# n = int(input('Введите число: '))
# result = hanoi_moves(n)
# print(f"Для n = {n}, число перестановок равно {result}")