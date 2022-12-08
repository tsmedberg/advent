file = open("day8/input")
lines = file.readlines()
grid = []
visible = 0
maxScenic = 0
for line in lines:
    grid.append(list(map(int, list(line.replace("\n", "")))))
def isVisible(x, y):
    if (y == 0 or y == len(grid) - 1) or (x == 0 or x == len(grid[y]) - 1):
        return True
    global maxScenic
    treeHeight = grid[y][x]
    leftVisible = True
    rightVisible = True
    topVisible = True
    bottomVisible = True
    right = len(grid[y]) - 1 - x
    left = x
    top = y
    bottom = len(grid) - 1 - y
    for i in range(x - 1, -1, -1):
        if grid[y][i] >= treeHeight:
            leftVisible = False
            left = x - i
            break
    for i in range(x + 1, len(grid[y])):
        if grid[y][i] >= treeHeight:
            rightVisible = False
            right = i - x
            break
    for i in range(y - 1, -1, -1):
        if grid[i][x] >= treeHeight:
            topVisible = False
            top = y - i
            break
    for i in range(y + 1, len(grid)):
        if grid[i][x] >= treeHeight:
            bottomVisible = False
            bottom = i - y
            break
    scenic = right * left * top * bottom
    if scenic > maxScenic:
        maxScenic = scenic
    return leftVisible or rightVisible or topVisible or bottomVisible
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if isVisible(x, y):
            visible = visible + 1
print("visible", visible)
print("max scenic", maxScenic)