#Shaylee McBride
#25Apr2018
#longestWord.py

words = input('Enter some words: ').split(' ')

longest = 0
for item in words:
    if longest < len(item):
        longest = len(item)
        
for item in words:
    if len(item) == longest:
        print(item)