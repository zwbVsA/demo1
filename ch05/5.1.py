a = 1, 2, '张文博'
print(a)
x, y, z = a
print(x, y, z)

c = d = e = '汇付天下'
print(c, d, e, id(c), id(d), id(e))

print(bool(""))
print(bool([]))
print(bool({}))
print(bool(tuple()))
