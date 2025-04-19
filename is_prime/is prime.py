"""
#* Target --> build program thet check if the given number is prime or not
"""
def get_user_input():
    while True:
        try:
            number = int(input("Enter a Positive Integer number: "))
            if number <= 0:
                print("Zero or Any negative number is no Prime Try again: ") 
            else:
                break
        except(ValueError):
            print("Invailed Input !!")
    return number

def is_prime(number):
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    triple = 0

    if number < 10:
        for x in lis[:number]:
            if number % x == 0:
                triple += 1
            else:
                continue
    
    if number > 10:
        triple += 1 
        for x in lis:
            if number % x == 0:
                triple += 1
            else:
                continue

    if triple < 2:
        return f"Number 1 is absolutly a non prime number"
    elif triple == 2:
        return f"Number {number} is a prime number"
    else:
        return f"Number {number} is not a prime number"
    
def repeat():
    while True:
        number = get_user_input()
        print(is_prime(number))
        trail = str(input("do you want to try again [y] Yes [any other key] No: "))
        if trail.lower() != "y":
            print("----- # See You Later # -----")
            break

repeat()