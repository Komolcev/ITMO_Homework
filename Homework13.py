# #13-1:
# def gen():
#     num = 1
#     while True:
#         yield num
#         num += 1
#         yield -num
#         num += 1
# g = gen()
# for _ in range(10):
#     print(next(g))



#13-2:
# def palin(num):
#     return str(num) == str(num)[::-1]
# def gen():
#     num = 1
#     while True:
#         if palin(num):
#             yield num
#         num += 1
# g = gen()
# for _ in range(50):
#     print(next(g))



# # 13-3:
# def odd_numbers(input_list):
#     for num in input_list:
#         if num % 2 != 0:
#             yield num
# input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# g = odd_numbers(input_numbers)
# for num in g:
#     print(num)