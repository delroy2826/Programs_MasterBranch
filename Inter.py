
user_input= input("Enter two numbers seprated by comma:")
user_input_split=user_input.split(",")
number1 =user_input_split[0]
number2=user_input_split[1]
if int(number1)>int(number2):
    for i in range(int(number1)):
        val = str(i)[::-1]
        if int(number1) == i + int(val):
            print("Got it", i, int(val))
            break
else:
    for i in range(int(number2)):
        val = str(i)[::-1]
        if int(number2) == i + int(val):
            print("Got it", i, int(val))
            break