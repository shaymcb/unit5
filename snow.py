#Shaylee McBride
#30Apr2018
#snow.py

from ggame import *
from random import randint

FLAKES = 2
RATE = 20
WIDTH = 1000
HEIGHT = 560

def step():
    data['frames'] += 1
    if data['frames']%RATE == 0:
        for i in range(FLAKES):
            data['snowList'].append(Sprite(data['flake'],(randint(0,WIDTH),0)))
    for flake in data['snowList']:

        if flake.y < HEIGHT - 20:
            flake.x += randint(-4,3)
            flake.y += randint(0,3)

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
    for i in range(FLAKES):
        data['snowList'].append(Sprite(data['flake'],(randint(0,WIDTH),0)))
    
    App().run(step)
