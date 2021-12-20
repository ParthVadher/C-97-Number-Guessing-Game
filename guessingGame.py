import random

ogNumber = random.randint(1,9)

chances = 0
while (chances < 5):
    

    guess = int(input("Guess a number between 1 and 9 : "))





    if(guess != ogNumber) :
        if(guess - ogNumber < 4 and guess - ogNumber > -4):
            print("Close,")
        if(guess - ogNumber > 4 or guess - ogNumber < -4):
            print("Too Far!")
        print(" Try again")
    else :
        print("Congratulations!!! You have won")
        chances =5
    chances = chances + 1

print("The Original number was" + " " + str(ogNumber))
