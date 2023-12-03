# 26-1:
def compare_strings(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    if str1 == str2:
        return True
    if abs(len_str1 - len_str2) > 1:
        return False
    index1 = 0
    index2 = 0
    while index1 < len_str1 and index2 < len_str2:
        if str1[index1] != str2[index2]:
            break
        index1 += 1
        index2 += 1
    if len_str1 != len_str2:
        if len_str1 > len_str2:
            index1 += 1
        else:
            index2 += 1
    return str1[index1:] == str2[index2:]


print(compare_strings('abc', 'abc'))
print(compare_strings('abc', 'abcd'))
print(compare_strings('bc', 'abc'))
print(compare_strings('axc', 'abc'))
print(compare_strings('abc', 'acb'))
print(compare_strings('abc', 'a'))
print(compare_strings('', '  '))


# # 26-2:
# def dis(self):
#     for attr, value in self.__dict__.items():
#         print(f"{attr}: {value}")
# Pet = type('Pet', (), {'dis': dis})
# my_pet = Pet()
# my_pet.name = 'Tom'
# my_pet.age = 3
# my_pet.dis()


# # 26-3:
# class Person:
#     def __init__(self):
#         self._age = None
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self, value):
#         if 1 <= value <= 100:
#             self._age = value
#         else:
#             print("Недопустимый возраст")
#     @age.deleter
#     def age(self):
#         print("Удаление возраста")
#         del self._age
# person = Person()
# person.age = 25
# print(person.age)
# person.age = 120
# del person.age
