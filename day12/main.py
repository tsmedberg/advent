import math
file = open('day12/input')
lines = file.readlines()
start = [0,0]
end = [0,0]
def charToHeight(char):
    return ord(char)-97
def distance(p1,p2):
    return int(math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2))
def isPossible(pos,curHeight):
    return curHeight -1 <= charToHeight(lines[pos[0]][pos[1]]) <= curHeight +1
for y in range(len(lines)):
    lines[y]=lines[y].replace('\n','')
    for x in range(len(lines[y])):
        char = lines[y][x]
        if char == 'S':
            start = [y,x]
        elif char == 'E':
            end = [y,x]
print(start)
print(end)
foundEnd=False
def finder(pos,beenAt=[],fromStart = 0):
    if lines[pos[0]][pos[1]] == 'E':
        print('END')
    beenAt.append(pos)
    curHeight = charToHeight(lines[pos[0]][pos[1]])
    if curHeight == -14:
        curHeight = 0
    y,x = pos
    viablePositions =[[y,x+1],[y,x-1],[y+1,x],[y-1,x]]
    cost = 0
    costPoint = None
    for p in viablePositions:
        if p[0] < 0 or p[0] >= len(lines) or p[1] < 0 or p[1] >= len(lines[p[0]]):
            continue
        if p in beenAt or not isPossible(p,curHeight):
            continue
        else:
            d = distance(p,end)+fromStart
            print(d)
            if d > cost:
                cost = d
                costPoint = p
    if costPoint != None:
        finder(costPoint,beenAt,fromStart+1)

    
print(finder(start))