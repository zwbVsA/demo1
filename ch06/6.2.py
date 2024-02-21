def ss(x, y):
    """x + y"""
    print('函数before：',x,y,id(x),id(y))
    c=x
    x=y
    y=c
    #x, y = y, x
    print('函数after：', x, y,id(x),id(y))
    return x + y


x = 100
y = 4
print(type(x),type(y),id(x),id(y))
print(x,y)
ds = ss(x, y)
print(x,y)
print(ds)



