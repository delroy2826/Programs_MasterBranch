class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
        #print("One",l,b)
    def area(self):
        #print("Two",self.l,self.b)
        return self.l * self.b
    def perimeter(self):
        #print("Three",self.l,self.b)
        return 2*(self.l+self.b)
class Square(Rectangle):
    def __init__(self,l):
        #print("One",l,l)
        super().__init__(l,l)
class Square1(Square):
    def __init__(self,l):
        #print("One",l)
        super().__init__(l)
s=Square1(10)
print(s.area())
print(s.perimeter())
s1 = Square(5)
print(s1.area())
print(s1.perimeter())
r = Rectangle(5,10)
print(r.area())
print(r.perimeter())