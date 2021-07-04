def pizza_menu():
    print("WELCOME TO PIZZA SECTION!!!! hope you enjoy")
    
    menu=[[1,'A',210,250,280],
         [2,'B',260,300,1000],
         [3,'C',560,340,500],
         [4,'D',450,550,650]]
    print('WHIC PIZZA DO YOU WANT TO ORDER')
    print('-----------------------------------------------------')
    print('sl.no                       pizza                    ')
    print('-----------------------------------------------------')
    for i in menu:
        print()
        print(i[0],'                  ',i[1])
        print('                small       medium         large  ')
        print('                ',i[2],'   ',i[3],'         ',i[4])
    print('---------------------------------------------------------')
    
    a=True
    t=[]
    l=[]
    c=input('Wich categaroy of pizza do you want')
    while c:
        if c=='1':
            print()
            print('For Samll pizza press S')
            print('For Medium pizza press M')
            print('For Large pizza press L')
            print()
            t.append('A')
            size=input('Which size of piza do you want')
            if size=='s':
                t.append('SMALL')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*210)
                l.append(t)
            elif size=='m':
                t.append('medium')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*250)
                l.append(t)
            elif size=='l':
                t.append('LARGE')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*300)
                l.append(t)
        elif c=='2':
            print()
            print('For Samll pizza press S')
            print('For Medium pizza press M')
            print('For Large pizza press L')
            print()
            t.append('B')
            size=input('Which size of piza do you want')
            if size=='s':
                t.append('SMALL')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*210)
                l.append(t)
            elif size=='m':
                t.append('medium')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*250)
                l.append(t)
            elif size=='l':
                t.append('LARGE')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*300)
                l.append(t)
        elif c=='3':
            print()
            print('For Samll pizza press S')
            print('For Medium pizza press M')
            print('For Large pizza press L')
            print()
            t.append('C')
            size=input('Which size of piza do you want')
            if size=='s':
                t.append('SMALL')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*210)
                l.append(t)
            elif size=='m':
                t.append('medium')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*250)
                l.append(t)
            elif size=='l':
                t.append('LARGE')
                n=int(input('How many pizza do you want'))
                t.append(n)
                t.append(n*300)
                l.append(t)
        elif c=='4':          
               print()
               print('For Samll pizza press S')
               print('For Medium pizza press M')
               print('For Large pizza press L')
               print()
               t.append('D')
               size=input('Which size of piza do you want')
               if size=='s':
                    t.append('SMALL')
                    n=int(input('How many pizza do you want'))
                    t.append(n)
                    t.append(n*210)
                    l.append(t)
               elif size=='m':
                    t.append('medium')
                    n=int(input('How many pizza do you want'))
                    t.append(n)
                    t.append(n*250)
                    l.append(t)
               elif size=='l':
                    t.append('LARGE')
                    n=int(input('How many pizza do you want'))
                    t.append(n)
                    t.append(n*300)
                    l.append(t)      
        else:
          c=input("INVALID OPTION DO YOU WISH TO CONTINUE IF YES PRESS Y")
          if c!='y':
              print("Thank you for vsiting")
              a=False
              break
          else:
              pizza_menu()
        a=False
        return l
        
        
    
a=True
n=''
while a:
    name=input("Enter the name:  ")
    if name=='':
        print("Invalid name!!!!!!!!!!!")
        c=input("Do you want to continue !!!! if yes press y: ")
        if c!='y':
            print("Thank you for visiting")
            a=False
            break
        else:
            continue
    n+=name
    a=False

    print()
    print("Dominous".center(80,'*'))
    print()
    print("welcome ME/Mrs",n,"To Dominoas")
    print("---------------------------------------------------")
    print()
    
    first_view=[[1,'pizza'],
                [2,'Drinks'],
                [3,'Sandwich'],
                [4,'Dessert']]
    print("WHICH CATEGAROY DO YOU WANT TO CHOOSE")
    print()
for i in first_view:
     print(i[0],' ',i[1])

amount=0
bill1=[]
bill=0
c=input("Enter the card serial number")
print()
if c.isdecimal:
        if c=='1':
            z=True
            while z:
                bill=pizza_menu()
                bill1.append(bill[0])
                print('****************',bill,'****************')
            
                if input('DO YOU WANT OT ORDER MORE PIZZA IF YES PRESS Y')!='y':
                    for i in bill:
                        amount+=i[-1]
                    z=False
        elif c=='2':
            pass
        elif c=='3':
            pass
        elif c=='4':
            pass
        else:
            print("Invalidoption")
        print("The Total Amount is : ",amount)