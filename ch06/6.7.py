def f1(c, f):
    def f2():
        return f(c)
    return f2


print(f1(-100, abs)())
