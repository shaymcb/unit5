#Shaylee McBride
#5/1/18
#sortingTemplate.py - times a sorting function

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def mergesort(A,B,n):
    B = A
    splitmerge(B,0,n,A)

def splitmerge(B,iBegin,iEnd,A):
    if iEnd - iBegin < 2:
        return A
    iMiddle = (iEnd - iBegin)/2
    splitmerge(A, iBegin, iMiddle, B)
    splitmerge(A, iMiddle, iEnd, B)
    merge(B, iBegin, iMiddle, iEnd, A)

def merge(A, iBegin, iMiddle, iEnd, B):
    
    
if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = quicksort(numbers, 0, len(numbers)-1)
    #numbers = numbers.sort()
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')


