class Cc:
    def __init__(self,name):
        self.name=name

    #def __str__(self):
    #    return self.name

    def __repr__(self):
        return self.name


c = Cc("苹果")
print(c,str(c))