#Python Program to Calculate Profit or Loss using Elif Statement
acost = 160
sale =170
if sale < acost:
    print("Loss is",acost-sale)
elif sale >acost:
    print("Profit is ",sale-acost)
else:
    print("No lost and No Profit")