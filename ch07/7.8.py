class myClass:
    def __init__(self):
        pass
    def handle(self):
        print("no arg")
    def handle(self,x):
        print("1 arg",x)
    def handle(self,x,y):
        print("2 arg",x,y)
    def handle(self,x,y,z):
        print("3 arg",x,y,z)

x=myClass()
x.handle(1,2,3)
x.handle(1)