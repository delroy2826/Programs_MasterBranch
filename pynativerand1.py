#Question 1: Generate 3 random integers between 100 and 999 which is divisible by 5
import random
for i in range(3):
    a=random.randrange(100,999,5)
    print(a)