'''
class MathUtils:

    @staticmethod
    def average(a, b):
        return a + b / 2

print(MathUtils.average(2, 1))'''

class MathUtils:

    @staticmethod
    def average(a, b):
        return (a + b) / 2

print(MathUtils().average(2, 1))
#3
n1 = int(input())
n2 = int(input())
print((n1+n2)/2)