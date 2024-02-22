class A:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print("这是A类的printName函数,name = %s" % self.name)


class B(A):
    def __init__(self, name):
        A.__init__(self, name)

    def printName(self):
        print("这是B类的printName函数,name = %s" % self.name)


class C(B):
    def __init__(self, name):
        B.__init__(self, name)

    def printName(self):
        print("这是C类的printName函数,name = %s" % self.name)


print(A("王小玲").printName())

print(B("张一飞").printName())

print(C("刘天佑").printName())
