# Get a number from User, then find the square of it, iterate it via while loop from number^2 to and print number for each loop

numberFromUser = int(input("Enter a number:"))

squareOfNumber = numberFromUser * numberFromUser

while (squareOfNumber > 0):
    squareOfNumber = squareOfNumber - 1 
    print(squareOfNumber)