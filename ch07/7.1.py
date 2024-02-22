class Fruits:
    """定义水果的类"""
    fruCount=0

    def __int__(self,name,price):
        self.name = name
        self.price = price
        Fruits.fruCount += 1

    def displayFruits(self):
        Fruits.fruCount += 1
        print("这是一个水果类的例子")
        print("名称：",self.name,",价格：",self.price)


