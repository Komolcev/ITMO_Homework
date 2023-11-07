class A:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit <= 0:
            raise StopIteration
        else:
            self.limit -= 1
            return self.limit


b = A(5)
for i in b:
    print(111, i)
    # print(222,  next(b))
    # print(333,  next(b))
# StopIteration выскочил потому, что некст явный
