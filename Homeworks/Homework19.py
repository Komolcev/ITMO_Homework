# # 19-1:
# import itertools

# money = [50, 100, 200, 500, 1000, 5000]

# all_money = []
# for i in range(1, len(money) + 1):
#     combs = itertools.combinations(money, i)
#     for comb in combs:
#         summ = sum(comb)
#         all_money.append(summ)


# all_money = list(set(all_money))
# all_money.sort()

# print(all_money)


# # 19-2:
# class Fibonacci:
#     def __init__(self):
#         self.previous = 0
#         self.current = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         result = self.current
#         self.current = self.previous + self.current
#         self.previous = result
#         return result


# fib = Fibonacci()

# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))


# 19-3:
class Person:
    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic

    def __str__(self):
        reversed_last_name = self.last_name[::-1]
        reversed_first_name = self.first_name[::-1]
        reversed_patronymic = self.patronymic[::-1]
        full_name_reversed = f"{reversed_patronymic}{reversed_first_name}{reversed_last_name}"
        return full_name_reversed


p = Person('Иванов', 'Михаил', 'Федорович')
print(p)
me = Person('Сотникова', 'Евгения', 'Олеговна')
print(me)
