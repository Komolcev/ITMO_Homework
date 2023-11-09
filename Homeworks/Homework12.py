# 12-1:
def f(lst):
    min_x = min(lst)
    max_x = max(lst)
    min_ind = [i for i, x in enumerate(lst) if x == min_x]
    max_ind = [i for i, x in enumerate(lst) if x == max_x]
    return min_ind, max_ind


x = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
min_ind, max_ind = f(x)
print(min_ind, max_ind)


# 12-2:
x = 10
print(*[i for i in range(1, x + 1) for j in range(i)])


# 12-3:
def num(s):
    ranges = s.split(',')
    numbers = []
    for i in ranges:
        start, end = i.split('-')
        start = int(start)
        end = int(end)
        numbers += list(range(start, end + 1))
    return numbers


s = '1-2,4-4,3-6'
print(num(s))
