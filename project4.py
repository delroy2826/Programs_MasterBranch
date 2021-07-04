def pizza_menu():
    print("While to pizza section !!! Hope you enjoy it")

    menu=[[1,'A',250,290,340],
          [2,'B',270,310,360],
          [3,'C',290,330,380],
          [4,'D',310,350,400]]
    print("Which Pizza Do You want to order")
    print('----------------------------------------------')
    print('SL.NO                       PIZZA             ')
    print("----------------------------------------------")
    for i in menu:
        print()
        print(i[0],'             ',i[1])
        print('         ',i[2],'     ',i[3],'           ',i[4])
    print('-'*25)
    a=True
    l=[]
    t=[]
    while a:
        c=input("Which category of pizza do you want")
        if c=='1':
            print()
            print("For small pizza press S ")
            print("For medium pizza press M")
            print("For large pizza Press L")
            print()
            t.append('A')
            size = input("Which Size of pizza do you want")
            if size == 's':
                t.append('SMALL')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*250)
                l.append(t)
            elif size == 'm':
                t.append('medium')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*290)
                l.append(t)
            elif size == 'l':
                t.append('Large')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*340)
                l.append(t)
        elif c=='2':
            print()
            print("For small pizza press S ")
            print("For medium pizza press M")
            print("For large pizza Press L")
            print()
            t.append('B')
            size = input("Which Size of pizza do you want")
            if size == 's':
                t.append('SMALL')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*270)
                l.append(t)
            elif size == 'm':
                t.append('medium')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*310)
                l.append(t)
            elif size == 'l':
                t.append('Large')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*360)
                l.append(t)
        elif c=='3':
            print()
            print("For small pizza press S ")
            print("For medium pizza press M")
            print("For large pizza Press L")
            print()
            t.append('C')
            size = input("Which Size of pizza do you want")
            if size == 's':
                t.append('SMALL')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*290)
                l.append(t)
            elif size == 'm':
                t.append('medium')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*330)
                l.append(t)
            elif size == 'l':
                t.append('Large')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*380)
                l.append(t)
        elif c=='4':
            print()
            print("For small pizza press S ")
            print("For medium pizza press M")
            print("For large pizza Press L")
            print()
            t.append('D')
            size = input("Which Size of pizza do you want")
            if size == 's':
                t.append('SMALL')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*310)
                l.append(t)
            elif size == 'm':
                t.append('medium')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*350)
                l.append(t)
            elif size == 'l':
                t.append('Large')
                n=int(input("How many pizza do you want"))
                t.append(n)
                t.append(n*400)
                l.append(t)
        else:
            b=input("Invalid opiton !!! Do you wish to continue if yes press y")
            if b!='y':
                print("Thank you for visiting us")
                a=False
                break
            else:
                pizza_menu()
        a = False
        return l
a = True
n=''
while a:
    global name
    name = input("Enter Your Name: ")
    if name == "":
        print("Invalid Name!!!")
        c=input("Do you want to continue.\nIf Yes Press y: ").lower()[0]
        if c!= 'y':
            print("Thank you for visiting Have a nice day")
            a = False
            break
        else:
            continue
    n+=name
    a = False
    print()
    print("Dominos".center(28,"*"))
    print()
    print("Welcome Mr/Mrs.",name,"To Dominos")
    print("-"*28)

    first_view=[[1,'Pizza'],[2,'DESSERT'],[3,'DRINKS'],[4,'SNACKS']]
    print("which category you want to choose")
    print()
    for i in first_view:
        print(i[0],'  ',i[1])
    amount=0
    bill1=[]
    bill =0
    c=input("Enter the card serial number")
    print()
    if c.isdecimal():
        if c=='1':
            z=True
            while z:

                bill=pizza_menu()
                bill1.append(bill[0])
                print('******',bill1,'********')

                if input("Do you want to order more pizza")!='y':
                    for i in bill1:
                        amount+=i[-1]
                    Z=False
        elif c == '2':
            pass
        elif c== '3':
            pass
        elif c == '4':
            pass
    else:
        print("Invalid Input")
        print("The total amount is:",amount)
a=False