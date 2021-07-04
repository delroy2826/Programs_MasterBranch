class Calc():

    def fact(self,n,count):
        print(l)
        for i in range(1,n):
            if n%i==0:
                l.append(i)
                count+=i
        if count==n:
            print("Perfect Number",l,'=',n)
        else:
            print("Not Perfect Number",l,'!=',n)
d=Calc()
count=0
l=[]
n=6
d.fact(n,count)