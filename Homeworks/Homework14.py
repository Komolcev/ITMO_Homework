# # 14-1:
# def len_num(n):
#     if n < 10:
#         return 1
#     else:
#         return len_num(n // 10) + 1

# print(len_num(int(input('Введите число: '))))


# # 14-2:
# def sum_num(n):
#     if n < 10:
#         return n
#     else:
#         return sum_num(n // 10) + n % 10


# print(sum_num(int(input('Введите число: '))))


# 14-3:
# def tri_2(n):
#     if n == 1:
#         print('*')
#         return
#     print('*' * n)
#     tri_2(n - 1)
#     print('*' * n)
#     return


# n = int(input('n: '))
# tri_2(n)
