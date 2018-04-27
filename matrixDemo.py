#Shaylee McBride
#27Apr2018
#matrixDemo.py - lists inside lists

def printBoard(board):
    for r in range(3):
        for c in range(3):
            print(board[r][c],end=' ') #end changes seperation
        print() #starts new line with nothing in it

board = [['a','b','c'],['d','e','f'],['g','h','i']]
printBoard(board)

row = int(input('enter a row: '))
col = int(input('enter a column: '))

board[row-1][col-1] = 'X'
printBoard(board)
