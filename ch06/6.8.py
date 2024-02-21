def count():
    fs=[]
    for i in range(1,4):
        def f():
            print("i的值为：",i)
            return i * i
        fs.append(f)
    return fs

print(count())
f1,f2,f3 = count();
#print(dir(f1))
#print(dir(f2))
#print(dir(f3))
print(f1())
print(f2())
print(f3())

def count1():
    fs=[]
    for i in range(1,4):
        def g(a):
            f = lambda : a * a
            return f
        fs.append(g(i))
    return fs

f11,f22,f33 = count1();
print(f11())
print(f22())
print(f33())


def count2():
    fs=[]
    for i in range(1,4):
        def f(a):
            print("i的值为：",i)
            return a * a
        fs.append(f(i))
    return fs

print(count2())
f111,f222,f333 = count2();

