def fruits(aa,**args):
    print("aa内容为:",aa)
    print("请求参数为:",args)
    for key in args.keys():
        print("key值为：",key)
        print("value:",args[key])
    return


fruits('水果',苹果='3',香蕉=4,橘子=6)


