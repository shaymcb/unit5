#Shaylee McBride
#4May2018
#connectFour.py

from ggame import *

RADIUS = 40
SPACE = 10


if __name__ == "__main__":
    data = {}
    data['holelist'] = []
    
    white = Color(0xFFFFFF,1)
    yellow = Color(0xFFFF00,1)
    
    board = RectangleAsset((RADIUS*2*7+SPACE*8),(RADIUS*2*6+SPACE*7),LineStyle(1,yellow),yellow)
    hole = CircleAsset(RADIUS, LineStyle(1,white), white)
        
    Sprite(board)
    for i in range(6):
        for j in range(7):
            newHole = Sprite(hole, (SPACE*(j+1)+RADIUS*2*j,SPACE*(i+1)+RADIUS*2*i))
            data['holelist'].append(newHole)
    
    App().listenKeyEvent('A')
    
    App().run()


