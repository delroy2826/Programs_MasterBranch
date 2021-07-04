import random
total_amount=0
item_amount1=[]
item_amount2=[]
item_amount3=[]
item_amount4=[]
bill1=0
bill2=0
bill3=0
bill4=0
def pizza_menu():
    menu=[[1,'pepper barbecue',165,200,350],
          [2,'chicken sausage',165,200,350],
          [3,'margherita     ',165,200,350],
          [4,'cheese & corn  ',165,200,350]
          ]
    print("*".center(80,'*'))
    print("\ns.no       pizza                    small        medium       large".upper())
    print("=".center(80,'='))
    for i in menu:
        print(*i,sep="          ")
    print()
    print("*".center(80,'*'))
    cart=[]
    temp=[]
    choice=input("Enter the desired pizza number--->")
    if choice=="1":
        temp.append("pepper barbecue")
        size=input("Enter the desired pizza size\ns for small\nm for medium\nl for large\n--->")
        if size=="s":
            temp.append("small")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*165)
            cart.append(temp)
        elif size=="m":
            temp.append("medium")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*200)
            cart.append(temp)
        elif size=="l":
            temp.append("large")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*350)
            cart.append(temp)
    elif choice=="2":
        temp.append("chicken sausage")
        size=input("Enter the desired pizza size\ns for small\nm for medium\nl for large\n-->")
        if size=="s":
            temp.append("small")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*165)
            cart.append(temp)
        elif size=="m":
            temp.append("medium")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*200)
            cart.append(temp)
        elif size=="l":
            temp.append("large")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*350)
            cart.append(temp)
    elif choice=="3":
        temp.append("margherita")
        size=input("Enter the desired pizza size\ns for small\nm for medium\nl for large\n--->")
        if size=="s":
            temp.append("small")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*165)
            cart.append(temp)
        elif size=="m":
            temp.append("medium")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*200)
            cart.append(temp)
        elif size=="l":
            temp.append("large")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*350)
            cart.append(temp)
    elif choice=="4":
        temp.append("cheese & corn")
        size=input("Enter the desired pizza size\ns for small\nm for medium\nl for large\n---->")
        if size=="s":
            temp.append("small")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*165)
            cart.append(temp)
        elif size=="m":
            temp.append("medium")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*200)
            cart.append(temp)
        elif size=="l":
            temp.append("large")
            number=int(input("how many pizza's?"))
            temp.append(number)
            temp.append(number*350)
            cart.append(temp)
    else:
        reply=input("Invalid option \n\nDo you wish to continue: \nIf yes press y\tIf no press any key \n--->")
        if reply!="y":
            print("Thankyou for visiting")
            return
        else:
            pizza_menu()
    return cart
def bread_menu():
    menu=[[1,'garlic breadsticks',95],
          [2,'chicken parcel    ',39],
          [3,'veg parcel        ',35],
          [4,'stuffed garlic    ',139]
          ]
    print("*".center(80,'*'))
    print("\ns.no       bread                    price".upper())
    print("=".center(80,'='))
    for i in menu:
        print(*i,sep="          ")
    print()
    print("*".center(80,'*'))
    cart=[]
    temp=[]
    choice=input("Enter the desired bread number")
    if choice=="1":
        temp.append('garlic breadsticks')
        number=int(input("how many breads?"))
        temp.append(number)
        temp.append(number*95)
        cart.append(temp)
    elif choice=="2":
        temp.append("chicken parcel")
        number=int(input("how many breads?"))
        temp.append(number)
        temp.append(number*39)
        cart.append(temp)
    elif choice=="3":
        temp.append("veg parcel")
        number=int(input("how many breads?"))
        temp.append(number)
        temp.append(number*35)
        cart.append(temp)
    elif choice=="4":
        temp.append("stuffed garlic")
        number=int(input("how many bread?"))
        temp.append(number)
        temp.append(number*139)
        cart.append(temp)
    else:
        reply=input("Invalid option \n\nDo you wish to continue: \nIf yes press y\tIf no press any key \n--->")
        if reply!="y":
            print("Thank you for visiting")
            return
        else:
            bread_menu()
    return cart
def pasta_menu():
    menu=[[1,'veg italiano   ',135],
          [2,'nonveg italiano',145],
          ]
    print("*".center(80,'*'))
    print("\ns.no       pasta                    price".upper())
    print("=".center(80,'='))
    for i in menu:
        print(*i,sep="          ")
    print()
    print("*".center(80,'*'))
    cart=[]
    temp=[]
    choice=input("enter the desired bread number")
    if choice=="1":
        temp.append('veg italiano')
        number=int(input("how many breads?"))
        temp.append(number)
        temp.append(number*135)
        cart.append(temp)
    elif choice=="2":
        temp.append("nonveg italiano")
        number=int(input("how many pasta?"))
        temp.append(number)
        temp.append(number*145)
        cart.append(temp)
    else:
        reply=input("Invalid option \n\ndo you wish to continue: \nIf yes press y\tif no press any key \n--->")
        if reply!="y":
            print("Thankyou for visiting")
            return
        else:
            pasta_menu()
    return cart
def drink_menu():
    menu=[[1,'pepsi    ',39],
          [2,'coke     ',39],
          [3,'mirinda  ',39],
          [4,'lemonade ',19]
          ]
    print("*".center(80,'*'))
    print("\ns.no       drink              price".upper())
    print("=".center(80,'='))
    for i in menu:
        print(*i,sep="          ")
    print()
    print("*".center(80,'*'))
    cart=[]
    temp=[]
    choice=input("Enter the desired drink number")
    if choice=="1":
        temp.append('pepsi')
        number=int(input("How many drinks?"))
        temp.append(number)
        temp.append(number*39)
        cart.append(temp)
    elif choice=="2":
        temp.append("coke")
        number=int(input("How many drinks?"))
        temp.append(number)
        temp.append(number*39)
        cart.append(temp)
    elif choice=="3":
        temp.append("mirinda")
        number=int(input("How many drinks?"))
        temp.append(number)
        temp.append(number*39)
        cart.append(temp)
    elif choice=="4":
        temp.append("lemonade")
        number=int(input("How many drinks?"))
        temp.append(number)
        temp.append(number*19)
        cart.append(temp)
    else:
        reply=input("Invalid option \n\nDo you wish to continue: \nIf yes press y\tIf no press any key \n--->")
        if reply!="y":
            print("thankyou for visiting".upper())
            return
        else:
            drink_menu()
    return cart
condition=True

while condition:
    name=input("enter the name:  ".upper())
    if name=="":
        print("\ninvalid name")
        temp=input("do u want to continue??? \ny or n:\n")
        if temp!="y":
            print("thank you for visiting")
            condition=False
            break
        else:
            continue
    break
    print("DOMINO'S".center(80,"-"))
    print("Welcome To Domino's: MR/MRS/MISS." + name)
    print("=".center(80,'='))
    print("Choose your order\n")
    print("=".center(80,'='))
cond1=True
while cond1:
    categories=[[1,'PIZZA'],[2,'BREAD'],[3,'PASTA'],[4,'DRINKS']]
    print("=="*40)
    for i in categories:
        print(i[0],"        ",i[1])
    print("="*80)
    item_no=input("choose the category number:")
    if item_no=="1":
        cond2=True
        while cond2:
            items=pizza_menu()
            for i in items:
                item_amount1.append(i[-1])
                for i in item_amount1:
                    bill1+=i
                    if input("Want more pizza?\nif yes press y \t or press enter to go back\n")!="y":
                        cond2=False
                        break
                    else:
                        continue
    elif item_no=="2":
        cond2=True
        while cond2:
            items=bread_menu()
            for i in items:
                item_amount2.append(i[-1])
                for i in item_amount2:
                    bill2+=i
                    if input("Want more bread?\nif yes press y \t or press enter to go back\n")!="y":

                        cond2=False
                        break
                    else:
                        continue
    elif item_no=="3":
        cond2=True
        while cond2:
            items=pasta_menu()
            for i in items:
                item_amount3.append(i[-1])
                if input("Want more pista?\nif yes press y \t or press enter to go back\n")!="y":
                    for i in item_amount3:
                        bill3+=i
                        cond2=False
                        break
                else:
                    continue

    elif item_no=="4":
        cond2=True
        while cond2:
            items=drink_menu()
            for i in items:
                item_amount4.append(i[-1])
                if input("Want more drink?\nif yes press y \t or press enter to go back\n")!="y":
                    for i in item_amount4:
                        bill4+=i
                        cond2=False
                        break
                else:
                    continue
    else:
        print("Invalid Option")
        if input("Do u want to continue:\nif yes press y \t\t if no press n")!="y":
            print("Thankyou for coming \n have a nice day")
        else:
            continue
    main_menu=input("DO YOU WANT TO GO BACK TO MAIN MENU ?\nIF YES PRESS y \nor press enter to billing :")
    if main_menu!="y":
        print("Your order no is :{}".format(random.randint(1,200)))
    else:
        continue
    total_amount=bill1+bill2+bill3+bill4
    print("TOTAL AMOUNT OF YOUR ORDER IS :{} ".format(total_amount))
    cond1=False