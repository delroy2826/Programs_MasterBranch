#String characters balance Test
#stringBalanceCheck(yn, Pynative) = True
def check(str1,str2):
    for i in str1:
        if i in str2:
            a = True
        else:
            a = False
            print(False)
            break
    while a:
        print(True)
        break
str1 = 'yn'
str2 = 'Pynative'
check(str1,str2)