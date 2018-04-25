#Shaylee McBride
#25Apr2018
#dictionaryDemo.py - more list practice

words = ['computer','mortify','dog','firetruck','yes','python','cat','attacking']

words.sort()

num = int(input('What number word do you want? '))
if num<=0 or num>len(words):
    print('Invalid Number')
else:
    print(words[num-1])
