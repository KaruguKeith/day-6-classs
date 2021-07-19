#1. Declare a list of vowels 
#2. Colllect user input
#3. Define a function and then  pass a sentence user input as parameter
#4. use a for looop to iterate through the user input to crosscheck for vowels
#5. Put an if statement in loop
#6. Print the vowels from the user input


from typing import Set


def getVowels (userInput):
    vowels = Set ("AEIOU")
    userInput = input('Enter sentence ')

    for letter in userInput:
        if letter.upper() in vowels :
            print(letter)

getVowels(userInput)