#Create a Algorithm For ATM software which will accept a withdraw amount
#gives "Error" as an Output if the amount is invalid else gives no of minimum
#Notes needed
n = 1000
n2 = n
l2 = []
l = [50,100,200,500,2000][::-1]
count = 0
a = True
while a:
    for i in l:
        if n>=i:
            l2.append(i)
            n=n-i
            count+=1
            if sum(l2)==n2:
                print(l2)
                print(count)
                a = False
                break
            break

n=1250
n2=n
l = [50,100,200,500,2000][::-1]
count = 0
amount = 0
a = True
while a:
    for i in l:
        if n>=i:
            amount+=i
            n=n-i
            count+=1
            if amount == n2:
                print(amount)
                print(count)
                a=False
                break
            break
