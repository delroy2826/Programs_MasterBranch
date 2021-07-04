#1 Program
def is_fibonacci(check):
    list_of_values=[]
    for i in range(max(check)+1):
        if i>1:
            list_of_values.append(list_of_values[i-2]+list_of_values[i-1])
        else:
            list_of_values.append(i)
    for i in check:
        if i in list_of_values:
            print("True",i)
        else:
            print("False",i)
check=[6,2,3,8,4,9,10]
is_fibonacci(check)
#2 Program
def is_fibonacci(check):
    list_of_values=[]
    for i in range(max(check)+1):
        if i>1:
            list_of_values.append(list_of_values[i-2]+list_of_values[i-1])
        else:
            list_of_values.append(i)
    for i in check:
        if i in list_of_values:
            pass
        else:
            print("False")
            break
check=[6,2,3,8,4,9,10]
is_fibonacci(check)