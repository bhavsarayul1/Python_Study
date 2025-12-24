# Task 1 : Check if Number is Even or Odd

# input from user

num = int(input("Enter a number: "))

#condition statement

if num % 2 == 0:
    print("Entered number is even")
else:
    print("Entered number is odd")

# Task with ternary operator condition

print("Entered number is even") if num % 2 == 0 else print("Entered number is odd")