class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Mysingleton(Singleton):
    att = 1


a = Mysingleton()

b = Mysingleton()
print(id(a))
print(id(b))

print(a == b)

print(a.__dict__)


class Singleton1(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        _instance1 = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        _instance1.__dict__ = cls._state

        return _instance1


class Mysingleton1(Singleton1):
    attr1=1


c = Mysingleton1()

d = Mysingleton1()

print(id(c))
print(id(d))

print(c == d)

print(id(c.__dict__))
print(id(d.__dict__))


def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class Mysingleton2(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


e = Mysingleton2()
f = Mysingleton2()

print(id(e))
print(id(f))
print(e == f)
print(e.x)



