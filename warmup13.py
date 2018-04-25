#Shaylee McBride
#25Apr2018
#warmup13.py - list of 20 random numbers and some stuff

from random import randint

aList = []
for i in range(20):
    aList.append(randint(1,100))

print('Sum =',sum(aList))
print('Min =',min(aList))
print('Max =',max(aList))
