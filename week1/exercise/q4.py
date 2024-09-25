# GAME: 'Find the number', take input from user, if input > randomNumber then print number is lower
# otherwise number is higher, loop that until user find the number

import random as rn
num = rn.randrange(0,100)

newGame = 'YES'
userGuess = -1

while userGuess : 
    if newGame == 'YES':
        print("Find My Random Number")
        newGame='NO'
        continue
    else:
        userGuess = int(input("Your Guess:\n"))
        if userGuess > num:
            print("Picked number is less than your guess")
        if num > userGuess:
            print("Picked number is greater than your guess")
        if num == userGuess:
            print("You won! The number is ", num)
            break;
