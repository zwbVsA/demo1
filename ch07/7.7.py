class people:
    name = ' '
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说： 我%d 岁" % (self.name, self.age))


class student(people):
    grade = ' '

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说： 我%d 岁，我在读%d年级" % (self.name, self.age, self.grade))


class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫%s，我是一名人民教师，我演讲的主题是%s" % (self.name, self.topic))


class sample(student,speaker):
    a = ''

    def __init__(self, n, a, w, g, t):
        speaker.__init__(self, n, t)
        student.__init__(self, n, a, w, g)


test = sample("小孟",25,80,4,"加强网络安全策略")
test.speak()
print(dir(test))
print(test.__dict__)