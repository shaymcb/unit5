#Shaylee McBride
#7May2018
#quiz5.py

def penultimate(L):
    return L[-2]

def plusEquals(numbers, integer):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]+integer
    return numbers
  
def smallest(L):
    minimum = L[0]
    for num in L:
        if num < minimum:
            minimum = num
    return minimum

def decimalRange(small, large, count):
    rangeList = []
    num = small
    while num < large:
        rangeList.append(num)
        num += count
    return rangeList

print(penultimate([1,2,3,'yes',5]))
print(plusEquals([1,2,3,4,5],2))
print(smallest([1,2,3,-3,5]))
print(decimalRange(0.1,2.3,0.2))