#Shaylee McBride
#4May2018
#warmup15.py


def double(List):
    list2 = []
    for num in List:
        list2.append(float(num)*2)
    return(list2)

list1 = (input('Enter numbers: ')).split(' ')

print(double(list1))