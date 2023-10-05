# 8-1:
def genetics(arr1):
    i = 0
    while i < len(arr1) - 1:
        tek = arr1[i]
        sled = arr1[i+1]
        if (tek == "А" and sled == "Г") or (tek == "Г" and sled == "А"):
            arr1[i] = sled
            arr1[i+1] = tek
            i = i + 1
        if (tek == "Ц" and sled == "Т") or (tek == "Т" and sled == "Ц"):
            arr1.insert(i+1, "А")
            arr1.insert(i+2, "Г")
            i = i + 2
        i = i + 1
    return arr1


string = input("Введите строку кода заглавными русскими буквами: ")
arr1 = list(string)
print(''.join(genetics(arr1)))


# 8-2:
lst = [[1, 3], [0], [1], [14, 23, 5297], [44, 666], [7, 8, 9, 0, 10]]


def s(x):
    return (-len(x), -sum(x))


lst.sort(key=s)
for i in lst:
    i.sort(reverse=True)
print(lst)


# 8-3:
lst = ['abab', 'xx', 'aaaaaaa', 'abcbab']
lst2 = sorted(lst, key=lambda x: (-len(set(x)), x))
print(lst2)
