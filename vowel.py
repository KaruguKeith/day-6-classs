def vowelCounting(str):

    str = input('Enter sentence : ')

    vowel  = set("aeiouAEIOU")

    vowelCount = 0

    for i in str :
         if i in vowel:
            vowelCount+=1

    print('The number of vowels are ' , vowelCount , sep =' ')

vowelCounting(str)