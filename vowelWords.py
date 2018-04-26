#Shaylee McBride
#26Apr2018
#vowelWords.py - demo that prints words that start with vowels (treat strings as lists)

words = input('Enter some words: ').split(' ')

for item in words:
    if item[0] in 'aieouAEIOU':
        print(item)
