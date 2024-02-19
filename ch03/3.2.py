dd = {'名称': '冰箱', '产地': '北京', '价格': '6500'}
print(dd)

print(dd['名称'])
# print(dd['尺寸'])

dd['名称'] = '洗衣机'
print(dd)

del dd['名称']
print(dd)

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
print(dir({}))

# len
print(len(dd))

print(dd.get('名称'))

print(dd.keys())
print(dd.values())

print(dd.pop('产地'))
print(dd)

dd = {'名称': '冰箱', '价格': '6500','产地': '北京'}
print(dd.popitem())
print(dd)



print(str(dd))


ee = dd.copy()
print(ee,dd)
ee['尺寸']='100'
print('ee:',ee)
print('dd:',dd)


print("品牌",dd.get('品牌','中国'))

print(dd.items())

sd = dd.setdefault('名称','电脑')
print(sd)
print(dd)

sd1=dd.setdefault('品牌','dell')
print(sd1)
print(dd)

dd.update({'产地':'上海','名称':'电脑'})
print(dd)








