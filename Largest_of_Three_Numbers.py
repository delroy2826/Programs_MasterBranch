#Python Program to find Largest of Three numbers using Elif Statement
n1 = 10
n2 = 7
n3 = 8
if n1 > n2 and n1>n3:
    print("1.) {} is greater than {} and {}".format(n1,n2,n3))
elif n2 > n1 and n2 > n3:
    print("2.) {} is greater than {} and {}".format(n2,n1,n3))
elif n3 >n1 and n3 >n1:
    print("3.) {} is greater than {} and {}".format(n3,n1,n2))
else:
    print("All Three Are Equal")

'''
n1 = 11
n2 = 10
n3 = 11

if n1>n2 and n1 > n3:
    print("n1")
elif n2>n1 and n2>n3:
    print("n2")
elif n3>n1 and n3>n2:
    print("n3")
elif n1==n2==n3:
    print("All ARE eQUAL")
elif n3<n1 and n1==n2:
    print("n1 AND n2 Are equal")
elif n2<n1 and n1==n3:
    print("N1 and N3 are equal")
elif n1<n2 and n2==n3:
    print("N2 and N3 are equal")'''