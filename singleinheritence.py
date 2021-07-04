class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
        #print("One",l,b)
    def area(self):
        #print("Two",self.l,self.b)
        return self.l*self.b
    def perimeter(self):
        #print("three",self.l,self.b)
        return 2*(self.l+self.b)
class Square(Rectangle):
    def __init__(self,l):
        super().__init__(l,l)
s=Square(10)
print(s.area())
print(s.perimeter())