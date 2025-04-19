"""
Target --> build a program thet calculate the Vowels letters in a word
#ToDo --> apply classes,constructors, Dictionaries 
"""

class CountVowels:

    def __init__(self):
        self.text = ''
        self.l_text = []
        self.vowels_count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        self.result = 0
        
    def get_user_input(self):
        self.text = input("Enter a string --> ")
        self.l_text = list(self.text)
    
    def operation(self):
        for char in self.l_text:
            if char.lower() in self.vowels_count:
                self.vowels_count[char.lower()] += 1
            else:
                continue
        self.result =sum(self.vowels_count.values())
            

    def display(self):
        print(f"your input text: \"{self.text}\"")
        print(f"your input in list: {self.l_text}")
        print(f"Total Vowels letter = {self.result}")
        print("--- # Details # ---")
        for vowel, count in self.vowels_count.items():
            print(f"Number of {vowel} = {count}")
    
word = CountVowels()
word.get_user_input()
word.operation()
word.display()
    