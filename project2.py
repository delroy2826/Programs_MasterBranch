import random
import string
print("Password Picker")
q =True
while q:
    z=0
    for i in range(3):
        common = random.choice(['a','b','c','e','z'])
        names  = random.choice(['qa','we','as','rt'])
        special_char = random.choice(string.punctuation)
        num = str(random.randint(100,900))
        a = random.choice(common)
        z+=1
        print(z,")","PASSWORD: ",common+names+special_char+num+a)
    print("Do you want to exit (Yes/No)")
    q = input("")
    if q == 'yes':
        q == False
        print("Thank You")
        break
    else:
        q == True
