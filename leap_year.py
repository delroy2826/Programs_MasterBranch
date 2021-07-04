n = 2018
if n%4==0 and n%100!=0 or n%400==0:
    print("Leap Year")
else:
    print("Not Leap Year")


year = [1996,2000,2004,2005,2002,2020]
for i in year:
    if i%4==0 and i%100!=0 or i%400==0:
        print("Leap Year",i)
    else:
        print("Not Leap Year",i)


for i in range(2000,2021):
    if i%4==0 and i%100!=0 or i%400==0:
        print("Leap year {} ".format(i))
year = [1996,2000,2004 ,2005,2002,2020]

print([f"Leap Year {i}" if i%4==0 and i%100!=0 or i%400==0 else f"Not a leap year {i}" for i in year])