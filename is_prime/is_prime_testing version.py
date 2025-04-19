"""
#* Target --> build program thet check if the given number is prime or not
# ! this copy contian print statments just for tesing
# ? the other copy without comments or test statments

"""
def get_user_input():
    while True:
        try:
            number = int(input("Enter a Positive Integer number: "))
            if number <= 0:
                print("Zero or Any negative number is no Prime Try again: ") # frist prime number is 2 so all numbers under 2 is not prime
            else:
                break
        except(ValueError):
            print("Invailed Input !!")
    return number

def is_prime(number):
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    triple = 0

    if number < 10:
        print(f"# {number} is Smaller than 10 ","First Check IF")
        for x in lis[:number]: # becouse we can't test prime numbers by dividing the number by a bigger one like 3 % n : n>3
            if number % x == 0:
                print(f"---> {number} % {x} = {number % x}")
                triple += 1
                print(f"triple = {triple}")
            else:
                continue
    
    if number > 10:
        print(f"# {number} is Bigger than 10 ","Second Check IF")
        triple += 1 # this plus one as a count of dividing a number by it self
        print (triple)
        for x in lis:
            if number % x == 0:
                print(f"---> {number} % {x} = {number % x}")
                triple += 1
                print(f"triple = {triple}")
            else:
                continue

    if triple < 2:
        return f"Number 1 is absolutly a non prime number" # as every number has a rational form "/1", eche number is divided by 1 normaly  
    elif triple == 2: # cause the prime number is accept division by 1 and it self only so the varibale triple must be 2 for prime numbers
        return f"Number {number} is a prime number"
    else:
        return f"Number {number} is not a prime number"
    
def repeat():   # for repeating the process 
    while True:
        number = get_user_input()
        print(is_prime(number))
        trail = str(input("do you want to try again [y] Yes [any other key] No: "))
        if trail.lower() != "y":
            print("----- # See You Later # -----")
            break

repeat()