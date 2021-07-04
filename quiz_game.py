def quiz(uans,cans):

    global score
    attempt = 0
    a = True

    while a and attempt < 2:

        if uans == cans:

            print("Correct Answer\n")
            score +=1
            a = False

        else:

            print("Wrong Answer")
            uans = input("Wrong Answer. Please Try again:")

            attempt+=1

    if attempt == 2:

        print("The correct answer  is:",cans)
q = True
while q:
    score = 0
    print("Mathematical Quiz\n")

    print("A. 12 + 24:")
    uans = input("Choose the correct Option:\nA)34\nB)38\nC)32\nD)36\n")
    quiz(uans.casefold(),'d')

    #print("Your Score is:",score)

    print("B. 12 * 24:")
    uans = input("Enter the number:\nA)164\nB)288\nC)296\nD)298\n")
    quiz(uans.casefold(),'b')

    #print("Your Score is:",score)

    print("C. 24/12:")
    uans = input("Enter the number:\nA)2\nB)3\nC)4\nD)6\n")
    quiz(uans.casefold(),'a')

    #print("Your Score is:",score)

    print("D. 12 - 24:")
    uans = input("Enter the number:\nA)-34\nB)-38\nC)-12\nD)-26\n")
    quiz(uans.casefold(),'c')

    #print("Your Score is:",score)

    print("E. 2-2+8:")
    uans = input("Enter the number:\nA)8\nB)6\nC)12\nD)4\n")
    quiz(uans.casefold(),'a')

    print("Your Score {} out of 5:".format(score))

    print("Do you want to try again: (Yes/No)")
    q = (input(""))
    if q == 'Yes':
        q = True
    else:
        q = False
        print("Thank You. Game Over")