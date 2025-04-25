def get_user_input():
    while True:
        try:
            number = int(input("Enter an Integer: "))
            if number < 0:
                print("Invalid Input !! number must be > zero.")
            else:
                break
        except ValueError:
            print("Invalid Input !!")
    return number

def operation(num):
    lis = list(str(num))
    lis = list(map(int,lis))
    print(lis)
    power = len(lis)
    ar_num = sum(map(lambda x : x** power, lis))
    if num == ar_num:
        return f"True Armstrong Number = {ar_num}"
    else:
        return f"None Armstrong Number"

number = get_user_input()
print(operation(number))
    