"""
Fizz/Buzz program

#* Target --> program to detect if the number is multiplies by 3 or 5 or both or none
#*        --> FizzBuzz if multiplies by both 3 & 5
#*        --> Fizz if muliplies by 3
#*        --> Buzz if muliplies by 5

# ToDo --> Apply functions, While loop, (try, except), control flow(if statment)
#! this is a plugin called better comments
"""
def get_user_input():
    while True:
        try:
            number = int(input("Enter an Integer number: "))
            if number < 0 or number > 100 :
                print("❌ Out of Range Number !!!")
            else:
                break
        except(ValueError):
            print("❌ Invalid Input !!!")
    return number

def check(num):
    return "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else \
        "Fizz" if num % 3 == 0 else \
        "Buzz" if num % 5 == 0 else \
        "Nither Fizz or Buzz"

def perform():
    numb = get_user_input()
    print(check(numb))

def newtrail():
    while True:
        trail = input("Do you want another try ? 🤔: \ [Y]yes  [any oher key]NO ")
        if trail == "Y" or trail == "y":
            perform()
        else:
            print(" === Game Over === ")
            break
    return trail

perform()
newtrail()