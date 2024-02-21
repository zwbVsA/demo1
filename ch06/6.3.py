def gg(x, y):
    return x - y


print(gg(200, 100))
print(gg(x=200, y=100))
print(gg(y=100, x=200))


def ss(name, price):
    """ 输出商品价格信息 """
    print("名称：", name)
    print("价格：", price)
    return


ss('电视机', price=1000)
ss(price=100, name='冰箱')
