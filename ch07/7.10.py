class Fruit:
    a = 600
    def storeVar(self,x=a):
        print(locals())
        return x

    def print(self):
        print(locals())
        print(Fruit.a)

f = Fruit()
print(f.storeVar())
Fruit.a = 200
print(f.storeVar())

f.print()

print(locals())