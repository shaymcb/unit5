#Shaylee McBride
#25Apr2018
#warmup13.py - list of 20 random numbers and some stuff

from random import randint

alist = []
for i in range(20):
    alist.append(randint(1,100))

print('Sum =',sum(alist))
print('Min =',min(alist))
print('Max =',max(alist))
