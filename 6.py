import random
from string import ascii_lowercase

def setupgrid(gridsize, numberofmines):
    emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]
    mines = getmines(emptygrid, numberofmines)
    for i, j in mines:
        emptygrid[i][j] = 'X'
    grid = getnumbers(emptygrid)

def showgrid(grid):
    gridsize = len(grid)
    horizontal = '   ' + (4 * gridsize * '-') + '-'
    # Print top column letters
    toplabel = '     '
    for i in ascii_lowercase[:gridsize]:
        toplabel = toplabel + i + '   '
    print(toplabel + '\n' + horizontal)
    # Print left row numbers
    for idx, i in enumerate(grid):
        row = '{0:2} |'.format(idx + 1)
        for j in i:
            row = row + ' ' + j + ' |'
        print(row + '\n' + horizontal)
    print('')

def playgame():
    gridsize = int(input("Enter gridsize:"))
    while gridsize <= 0:
        print ('Please enter a number greater than 0!')
        gridsize = int(input("Enter gridsize:"))
    mines = int(input("Enter number of mines:"))
    while mines >= gridsize:
        print ('Number of mines must be at least 1 less than the number of gridsize.')
        mines = int(input("Enter number of mines:"))
    currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]
    showgrid(currgrid)

playgame()
