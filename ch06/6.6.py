x = 100

def changex():
    x = 200
    return x


print(x)
print(changex())


def changeGx():
    global x
    print("before:",id(x))
    x = 200
    print("after:",id(x))
    return x

print("global")
print(x,id(x))
print(changeGx())
print(x,id(x))
