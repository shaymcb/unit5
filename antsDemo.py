#Shaylee McBride
#30Apr2018
#antsDemo.py - using lists with graphics

from ggame import *
from random import randint

ANTS = 10
WIDTH = 1000
HEIGHT = 600

if __name__ == "__main__":
    
    red = Color(0xFF0000, 1)
    ant = CircleAsset(20,LineStyle(1,red),red)
    
    for i in range(ANTS):
        Sprite(ant,(randint(0,WIDTH),randint(0,HEIGHT)))
    
    App().run()

