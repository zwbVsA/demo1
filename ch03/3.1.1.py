aa = "ab"
laa = [100, 200, 300, 400]
bb = [(x, y) for x in aa for y in laa]
print("aa:", aa)
print("laa:", laa)
print("bb:", bb)

a = (100,)
print(a)
b = (100)
print(b)

# a[1]=200
# print(a)

a = (100, 200, 300, 400)
print(a)
a = a[1], a[2], a[3]
print(a)

aaa = (100, 200)
bbb = ('河汉清且浅', '相去复几许')
ccc = aaa + bbb
print(ccc)

# print(ccc)

print(dir(tuple()))