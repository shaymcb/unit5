#Shaylee McBride
#25Apr2018
#betterColoredWindow.py

from ggame import *
from random import randint

outline = LineStyle(0,Color(0x000000,1))
colors = ['0xFF0000','0x0FF000','0x00FF00','0x000FF0','0x0000FF','0xFFF000','0x0FFF00','0x00FFF0','0x000FFF']


def mouseClick(event):
    color = colors[randint(0,len(colors)-1)]
    background = RectangleAsset(1200,600,outline,Color(color,1))
    Sprite(background)
    
App.listenMouseEvent('click',mouseClick)
App().run()
