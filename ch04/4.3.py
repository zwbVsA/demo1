a = '目前市场上%s的价格为每公斤%d元'
b = ('苹果', 20)
c = a % b
print(c)

print(a % ('橘子', 10))

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
print(dir(str))

str = "i can because I think I can"
str1 = '芒果'
print(str.capitalize(), str1.capitalize())

print(str.count('cau'))

print(str.find("cau"))

s2='*'
e1=('黄','沙','百','战')
print(s2.join(e1))

print(str.isalpha(),str1.isalpha())

print(str.upper(),str.lower())

print(str.title())

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
print(str.casefold())
print("ß".casefold())

print(str.center(50,'*'))

str2='  niha '
print(str2.expandtabs(5))

str2.strip()
#str2.rjust()

str2.format()


str1 = "I'm string literal"
str1_new = str1.format()
print(str1)
print(str1_new)
print('str1 id:{}'.format(id(str1)))
print('str1_new id:{}'.format(id(str1_new)))

str2 = "{} want to eat {}"
str2_new = str2.format('渔道', '苹果')
print('str2 id:{}, content:{}'.format(id(str2), str2))
print('str2_new id:{}, content:{}'.format(id(str2_new), str2_new))

str3 = "{1} want to eat {0}"
str3_new = str3.format('渔道', '苹果')
print('str3 id:{}, content:{}'.format(id(str3), str3))
print('str3_new id:{}, content:{}'.format(id(str3_new), str3_new))

dict1 = {'name': '渔道', 'fruit': '苹果'}
str4 = "{name} want to eat {fruit}"
str4_new = str4.format(name=dict1['name'], fruit=dict1['fruit'])
print('str4 id:{}, content:{}'.format(id(str4), str4))
print('str4_new id:{}, content:{}'.format(id(str4_new), str4_new))

str4 = '{{}}, {}'
print(str4.format('渔道'))

name_width = 10
price_width = 10
nested_fmt = '{{:<{}}}{{:>{}}}'.format(name_width, price_width)
print(nested_fmt)
print(nested_fmt.format("苹果", 5.98))


x=100
print(f'{x+100}')
print(100)

