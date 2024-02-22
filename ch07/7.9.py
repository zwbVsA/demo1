class Fruit:
    def __init__(self, value):
        self._n = value
        self.__n = value

    def __func(self):
        print(self._n + 1)


f = Fruit(8)
print(f._Fruit__n)
print(f._Fruit__func())
print(f.__dict__)
print(f._n)
print(f.__dir__())
