from math import sqrt
import math

class AlgebraInterpreter:
    def __init__(self):
        self.__annotations__ = {}
        self.__annotations__['add'] = lambda x, y: x + y
        self.__annotations__['sub'] = lambda x, y: x - y
        self.__annotations__['mul'] = lambda x, y: x * y
        self.__annotations__['div'] = lambda x, y: x / y
        self.__annotations__['pow'] = lambda x, y: x ** y
        self.__annotations__['sqrt'] = lambda x: x ** 0.5
        self.__annotations__['log'] = lambda x, base: math.log(x, base)
        self.__annotations__['sin'] = lambda x: math.sin(x)
        self.__annotations__['cos'] = lambda x: math.cos(x)
        self.__annotations__['tan'] = lambda x: math.tan(x)
        self.__annotations__['atan'] = lambda x: math.atan(x)
        self.__annotations__['atan2'] = lambda y, x: math.atan2(y, x)
        self.__annotations__['exp'] = lambda x: math.exp(x)
        self.__annotations__['abs'] = lambda x: abs(x)
        self.__annotations__['floor'] = lambda x: math.floor(x)
        self.__annotations__['ceil'] = lambda x: math.ceil(x)
        self.__annotations__['round'] = lambda x: round(x)
        self.__annotations__['mod'] = lambda x, y: x % y
        self.__annotations__['gcd'] = lambda x, y: math.gcd(x, y)
        self.__annotations__['lcm'] = lambda x, y: abs(x * y) // math.gcd(x, y)
        self.__annotations__['factorial'] = lambda x: math.factorial(x)
        self.__annotations__['binomial'] = lambda n, k: math.comb(n, k)
        self.__annotations__['permutation'] = lambda n, k: math.perm(n, k)
        self.__annotations__['permutation'] = lambda n, k: math.perm(n, k)
        self.__annotations__['combination'] = lambda n, k: math.comb(n, k)

        def distance(x1, y1, x2, y2):
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        def distance3d(x1, y1, z1, x2, y2, z2):
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


class BasicOperations:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def add(self):
        return self.x1 + self.y1

    def subtract(self):
        return self.x1 - self.y1

    def multiply(self):
        return self.x1 * self.y1

    def divide(self):
        return self.x1 / self.y1

    def power(self):
        return self.x1 ** self.y1

    def root(self):
        return self.x1 ** (1 / self.y1)

    def log(self):
        return math.log(self.x1, self.y1)

    def log10(self):
        return math.log10(self.x1)

    def log2(self):
        return math.log2(self.x1)

    def sqrt(self):
        return math.sqrt(self.x1)
