"""
Sum of Digits program / problem

#* Target --> Get the summition of input digits
#  #ToDo --> Apply map function, (split & isdigit) methodes
"""

def get_user_input():
    while True:
        num = input("Enter a Number: ")
        if num.isdigit():
            digits = list(num)
            break
        else:
            print("Invaild Input !!! ")  
    return digits

def calc(number):
    return sum(map(int, number))

number = get_user_input()
print("the summition is ",calc(number))
