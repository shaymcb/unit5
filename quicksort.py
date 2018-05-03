#Shaylee McBride
#5/1/18
#sortingTemplate.py - times a sorting function

from random import randint
from time import time

N = 1000 #how many numbers will be sorted

def quicksort(A,lo,hi):
    if lo < hi:
        p = partition(A,lo,hi)
        quicksort(A,lo,p-1)
        quicksort(A,p+1,hi)
    return A
    
def partition(A,lo,hi):
    pivot = A[hi]
    i = lo -1
    for j in range(lo,hi):
        if A[j] < pivot:
            i = i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[hi] = A[hi],A[i+1]
    return i+1
    
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

