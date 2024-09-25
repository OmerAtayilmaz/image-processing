# write a method to calculate factorial number for instance if input is 5 the result must be 120

userInput = int(input('Enter a number to find its factorial\n'))

def calculate_factorial(num):
    result = 1;
    for i in range(1, num+1):
        result *= i
    
    return result
     

myNumber = 5
print("Your Number is : " , myNumber)

factorialResult = calculate_factorial(userInput);

print("Factorial of {} is {}".format(myNumber, calculate_factorial(userInput)),factorialResult )