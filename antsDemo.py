#Shaylee McBride
#30Apr2018
#antsDemo.py - using lists with graphics

from ggame import *
from random import randint

ANTS = 50
WIDTH = 1000
HEIGHT = 540

#move each ant randomly up/down and left/right
def step():
    for ant in data['antList']:
        ant.x += randint(-4,3)
        ant.y += randint(-4,3)

#putting fire ants randomly on the screen
if __name__ == "__main__":
    
    data = {}
    data['antList'] = []
    
    red = Color(0xFF0000, 1)
    ant = CircleAsset(20,LineStyle(1,red),red)
    
    for i in range(ANTS):
        data['antList'].append(Sprite(ant,(randint(0,WIDTH),randint(0,HEIGHT))))
    
    App().run(step)

