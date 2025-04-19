"""
--> Factorial Calculation
#* A program for calculating the factorial of number given by user
"""

def get_user_input():
    while True:
        try:
            number = int(input("Enter an Integer [1 - 10]: "))
            if number < 1 or number > 10:
                print("Out of range number")
            else:
                return number
        except ValueError:
            print("Invalid Input !!")

def factorial(number):
    result = 1
    for x in range(1, number + 1):
        result *= x
    return result

number = get_user_input()
result = factorial(number)
print(f"Factorial of {number} is {result}")