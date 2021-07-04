#Providing Perfect change for the given amount
a=True
while a:
    amount = int(input("Enter the Amount: "))
    temp_amount = amount
    coin_in_account = sorted([1,2,5,10,20],reverse = True)
    count= 0
    coin_count=1
    index = 0
    while True:
        try:
            if coin_in_account[index]<=temp_amount:
                temp_amount-=coin_in_account[index]
                count+=coin_in_account[index]
                print("Coin_{} : {} ".format(coin_count,coin_in_account[index]))
                coin_count+=1
                index = 0
            elif count==amount:
                print("Total:",count)
                break
            else:
                index+=1
        except Exception:
            print("Available Change:",count)
            print("Sorry No Proper Change Available Change Available. Loss of {}".format(amount - count))
            break
    b = input("If You want to Try Again Press Y, or else Press Any Key: ").lower()
    if b=='y':
       pass
    else:
        a=False

'''
#Providing Perfect change for the given amount
amount = 31
temp_amount = amount
coin_in_account = [25,10,1]
count= 0
index = 0
while True:
    if coin_in_account[index]<=temp_amount:
        temp_amount-=coin_in_account[index]
        count+=coin_in_account[index]
        print(coin_in_account[index])
        index = 0
    elif count==amount:
        break
    else:
        index+=1'''