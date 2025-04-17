"""
Reverse a String

#* takes user string then display it reversed
"""

def take_user_input():
    lis = list(input("Enter a Text: "))
    return lis

def reversing(lista):
    string = ''
    lenth = len(lista)
    for x in range(lenth):
        string += lista[lenth-x-1]
    return string

def is_palindrome(text):
    rtext = list(reversed(text))
    if text == rtext:
        return "Is Palindrome"
    else:
        return "Not Palindrome"

def perform():
    first = take_user_input()
    print("The Reversed String: ", reversing(first))
    print(is_palindrome(first))
    iteration = True
    while iteration == True:
        repeat = input("Do you want to try again ? [Y]yes [any other key]No ? ")
        if repeat == "y" or repeat == "Y":
            perform()
        else:
            print("----- OVER -----")
        break

perform()