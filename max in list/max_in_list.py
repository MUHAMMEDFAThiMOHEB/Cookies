def get_user_input():
    lis = []
    while True:
        try:
            items_n = int(input("Enter an integer number: "))
            if items_n > 0 and items_n < 10:
                break
            else:
                print("list lenght is out of range ")
        except(ValueError):
            print("Invalid input!!!")
    for x in range(items_n):
        n_item = int(input("enter list element (number): "))
        lis.append(n_item)
    print(f"List length = {items_n} -- List = {lis} ")
    return lis

def maximum(lis):
    target = lis[0]
    for x in lis:
        if x > target:
            target = x
    return target

trail = get_user_input()
print(trail)
print("----- ### ----- ### -----")
print(f"the maximum number of the list is {maximum(trail)} .")