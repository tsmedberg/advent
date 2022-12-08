file = open('day8/input')
lines = file.readlines()
grid = []
visible = 0
maxScenic = 0
for line in lines:
    grid.append(list(map(int,list(line.replace('\n','')))))

def isVisible(x,y):
    if (y == 0 or y == len(grid)-1) or (x == 0 or x == len(grid[y]) -1):
        return True
    treeHeight = grid[y][x]
    leftVisible = True
    rightVisible = True
    topVisible = True
    bottomVisible = True
    for i in range(x):
        if grid[y][i] >= treeHeight:
            leftVisible = False
            break
    for i in range(len(grid[y])-1,x,-1):
        if grid[y][i] >= treeHeight:
            rightVisible = False
            break
    for i in range(y):
        if grid [i][x] >= treeHeight:
            topVisible = False
            break
    for i in range(len(grid)-1, y, -1):
        if grid [i][x] >= treeHeight:
            bottomVisible = False
            break
    return leftVisible or rightVisible or topVisible or bottomVisible

def scenicScore(x,y):
    treeHeight = grid[y][x]
    right = len(grid[y])-1-x
    left = x
    top = y
    bottom = len(grid)-1-y
    for i in range(x-1,-1,-1):
        if grid[y][i] >= treeHeight:
            left = x-i
            break
    for i in range(x+1,len(grid[y])):
        if grid[y][i] >= treeHeight:
            right = i-x
            break
    for i in range(y-1,-1,-1):
        if grid [i][x] >= treeHeight:
            top = y-i
            break
    for i in range(y+1,len(grid)):
        if grid [i][x] >= treeHeight:
            bottom = i-y
            break
    return right*left*top*bottom
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if isVisible(x,y):
            visible = visible+1
        scenic = scenicScore(x,y)
        if scenic > maxScenic:
            maxScenic = scenic
print('visible',visible)
print('max scenic',maxScenic)