#1
class Parrot():
    def fly(self):
        print("Parrot can Fly")
    def swim(self):
        print("Parrot can't Swim")
class Penguin():
    def fly(self):
        print("Penguin can't Fly")
    def swim(self):
        print("Penguin can Swim")

def fly_test(bird):
    bird.fly()
def swim_test(bird):
    bird.swim()

Bird = Parrot()
fly_test(Bird)
swim_test(Bird)

Bird = Penguin()
fly_test(Bird)
swim_test(Bird)

#2
class Windows():
    def copy(self):
        print("CTRL + C")
    def paste(self):
        print("CTRL +V ")
class Mac():
    def copy(self):
        print("CMD + C")
    def paste(self):
        print("CMD + V")
def function(mname):
    mname.copy()
    mname.paste()
w = Windows()
function(w)
m = Mac()
function(m)
