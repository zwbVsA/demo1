def fruits(aa, *args):
    print("aa内容：", aa)
    print("可变参数为：", args)
    for bb in args:
        print("可变参数为：", bb)
    return


print('不带可变参数')
fruits('西瓜')
fruits('橘子','苹果',16)
fruits('西瓜','苹果',16,'香蕉',6,'橙子',10)
