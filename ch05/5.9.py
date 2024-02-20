#for (index,item) in enumerate(1,20):
#    print(index,item)

a = 20
sums = 0
b = 1
while b <= 20:
    sums = sums + b
    b += 1
print(sums)


c=1
while c<=20:
    print(c,"小于20")
    c+=1
else:
    print(c,"大于等于20")


a='盈盈一水间,脉脉不得语'
for b in a:
    if b == '不':
        print('发现目标文字')
        break
else:
    print('没发现对应的文字')


