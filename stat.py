#Shaylee McBride
#26Apr2018
#stat.py

print('Type a list of numbers')
print('Enter q when done')
L = []
while True:
    num = input("")
    if num == 'q':
        break
    L.append(float(num))

L.sort
minimum = min(L)
maximum = max(L)
mean = sum(L)/len(L)

middle = len(L)//2
if middle == len(L)/2:
    median = (L[middle-1] + L[middle])/2
else:
    median = L[middle]

most = 0
for item in L:
    count = L.count(item)
    if count > most:
        most = count
        mode = item

print('Min =',minimum)
print('Max =',maximum)
print('Mean =',mean)
print('Med =',median)
print('Mode =',mode)

