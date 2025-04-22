"""
=== ## @ Fibonacci Sequence @ ## ===
ToDo: create a program that calculate the Fibonacci sequance given 2 numbers
? Should the start be from (0, 1) ???
! ---------------------------------------------------------------------------
"""
class FibonacciSequence:

    def __init__(self, fstart, estart, length):
        self.fstart = fstart
        self.estart = estart
        self.length = length


    def display(self):
        print(f"Series starts from {fstart}, {estart}")

    def operation(self):
        fibonlist = [self.fstart, self.estart]
        for x in range(self.length):
            next_fib = fibonlist[x] + fibonlist[x+1]
            fibonlist.append(next_fib)
        return fibonlist


def get_user_input():
    while True:
        try:
            f = int(input("Enter first start number: "))
            e = int(input("Enter second start number: "))
            end = int(input("Enter the length of the fibonacci list: "))
            return f, e, end
        except ValueError:
            print("Please enter valid integers.")

fstart, estart, length= get_user_input()
fibonacci = FibonacciSequence(fstart, estart, length)
fibonacci.display()
print(fibonacci.operation())