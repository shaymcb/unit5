#Shaylee McBride
#13Apr2018
#middleWord.py

words = input('Enter some words: ').split(' ')

middle = len(words)//2

if middle == len(words)/2:
    print(words[middle-1:middle+1])

else:
    print(words[middle])
