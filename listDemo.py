#Shaylee McBride
#13Apr2018
#listDemo.py - print out first and last word in a list

words = input('Enter some words: ').split(' ')

print("The first word was:",words[0])
print("The last word was:",words[-1])

#go through one at a time
for item in words:
    print(item)