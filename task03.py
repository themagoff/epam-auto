class New:
    def __init__(self, num):
        self.num = num
    def show(self):
        print(self.num)


class Newest(New):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def calc(self):
        return self.num1 + self.num2


try:
    x = 5 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя")
finally:
    print("Конец")


def my_decor(func):
    def inner(*args, **kwargs):
        print(args, kwargs)
        func()
    return inner

@my_decor
def main():
    print("Main function")


class Decor:
    def __init__(self, value):
        self._data = value
    @property
    def data(self):
        return self._data


gen = (x for x in range(1, 11))


import collections
Point = collections.namedtuple('Point', ['x', 'y', 'z'])
p1 = Point(x=1, y=2, z=3)
