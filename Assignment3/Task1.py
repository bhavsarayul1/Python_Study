# Task 1 : Calculate Factorial Using a Function

# Define function and calculate factorial using recursion

def factorial(number):
    if number == 1:
        return 1
    else:
        result = number * factorial(number-1)
        return result

#taking output from user
number = int(input("Enter a number: "))

#calls the function

print(f"Factorial of {number} is: {factorial(number)}")
