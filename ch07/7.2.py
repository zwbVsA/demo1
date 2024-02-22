class Fruit:
    name = ' '
    city = ' '
    __price = ' '

    def __init__(self, n, c, p):
        self.name = n
        self.city = c
        self.__price = p

    def displayFruit(self):
        print("%s产的%s很好吃。价格为%s元" % (self.city, self.name, self.__price))


f = Fruit('苹果', '天水', 8)
f.displayFruit()
print(f.name,f.city)
print(Fruit.__dict__)
print(Fruit.__module__)

f.name='葡萄'
f.color='红色'
f.displayFruit()
print(f.color)
