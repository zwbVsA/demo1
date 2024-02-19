aa = [12, '何当共剪西窗烛', 1.66, ['一夕轻雷落万丝', 3.66]]
bb = aa.index(1.66)
cc = aa.index('何当共剪西窗烛')
print(bb)
print(cc)

aa = [12, '何当共剪西窗烛', 1.66]
aa[3:] = ['却话巴山夜雨时', 1.12]
print(aa)

print(aa[2:2])

aa[2:2] = ['张文博']

print(aa)

aa[2:4] = ['汇付天下']
print(aa)

aa[2:2] = (199,)
print(aa)

aa[-1]=100
print(aa)

del aa[0]
print(aa)

del aa[:]
print(aa)

aa=[1,2,3]+[4,5,6]+[7,8,9]
print(aa)

#del aa[:]

#aa=[1,2,3]*3
#print(aa)

#del aa[:]
#aa = [None]*3
#print(aa)

print("长度：",len(aa))
print("最大值:",max(aa))

#列出列表的所有方法：'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
print(dir([]))

aa.clear()
print("clear:",aa)

aa.append(2)
aa.append('hello')
print("append",aa)

bb=aa.copy()
print("bb",bb)
bb[0]=100
bb[1]=99
print("bb-change:",bb)
print("bb-aa:",aa,bb)

print("count:",aa.count('hello'))

aa.extend(('q','b'));
print(aa)

e=aa.index(5)
print("index",e)











