class similarity():

    def __init__(self, string1, string2):
        self.string1 = string1.lower()
        self.string2 = string2.lower()
        self.lis1 = list(self.string1)
        self.lis2 = list(self.string2)

    def operation(self):
        slis = []
        sletters = 0
        if len(self.string1) >= len(self.string2):
            bigger = self.string1
            smaller = self.string2
        else:
            bigger = self.string2
            smaller = self.string1
        for x in smaller:
            if x in bigger:
                sletters += 1
                slis.append(x)
            else:
                continue
        print(f"Number of similar letters = {sletters}")
        print(f"similar letter = {slis} ~ lenght = {len(slis)}")
        similarperc = sletters / len(bigger)
        return f"The percentage of similarity = {similarperc} ~ {similarperc * 100}%"

def inputs():
    string1 = input("Enter First string: ")
    string2 = input("Enter second string: ")
    print(f"Text 1 = {string1}")
    print(f"Text 2 = {string2}")
    print(f"Text 1 in list = {list(string1)} ~ length = {len(string1)}")
    print(f"Text 2 in list = {list(string2)} ~ length = {len(string2)}")
    return string1, string2

def main():
    while True:
        arg = inputs()
        test = similarity(*arg)
        print(test.operation())
        antry = input(f"Do you want to try again ? [Y] Yes, [Any other key] NO ?! ")
        if antry.lower() not in ("y", "yes"):
            print("### -- SEE YOU LATER -- ###")
            break

main()