#Shaylee McBride
#30Apr2018
#snow.py

from ggame import *
from random import randint

RATE = 40  #how often to add a new flake: lower number = heavier snowfall
WIND = 4 #how much the snow whips around
WIDTH = 1000
HEIGHT = 560

#makes the snow fall, generates new flakes and stores them in a list
def storm():
    data['frames'] += 1
    if data['frames']%RATE == 0:
        data['snowList'].append(Sprite(data['flake'],(randint(0,WIDTH),0)))
    for flake in data['snowList']:
        if flake.y < HEIGHT - 20:  #this is all I could figure out for accumulation: stops at bottom
            if data['frames']%WIND ==0:
                flake.x += randint(-5,4) #flakes move randomly side to side
            flake.y += randint(0,3) #flakes do not fall at constant rate

#generates background and first snowflake
if __name__ == "__main__":
    data = {}
    data['snowList'] = []
    data['frames'] = 0
    data['accumulation'] = 0
    
    black = Color(0x000000,1)
    white = Color(0xFFFFFF, 1)
    background = RectangleAsset(WIDTH,HEIGHT,LineStyle(1,black),black)
    data['flake'] = CircleAsset(10,LineStyle(1,white),white)
    
    Sprite(background)
    data['snowList'].append(Sprite(data['flake'],(randint(0,WIDTH),0)))
    
    App().run(storm)
