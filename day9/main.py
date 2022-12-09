file = open("day9/input")
lines = file.readlines()
beenAt = ['0,0']
hx,hy = 0,0
tx,ty = 0,0
def touching():
    global hx,hy,tx,ty
    if ty < hy -1 or ty > hy+1:
        return False
    if tx < hx -1 or tx > hx+1:
        return False
    return True
for line in lines:
    dir = line[0]
    step = int(line.split(' ')[1])
    for i in range(step):
        if(not touching()):
            if hx != tx and hy != ty: #is diagonal
                if hx > tx:
                    tx = tx +1
                else:
                    tx = tx - 1
                if hy > ty:
                    ty = ty + 1
                else:
                    ty = ty - 1
            elif hx == tx: #horizontally aligned
                if hy > ty:
                    ty = ty + 1
                else:
                    ty = ty - 1
            else:
                if hx > tx:
                    tx = tx +1
                else:
                    tx = tx - 1
        string = str(tx)+','+str(ty)
        if not string in beenAt:
            beenAt.append(string)
        if dir == 'U':
            hy = hy + 1
        elif dir == 'D':
            hy = hy - 1
        elif dir == 'L':
            hx = hx - 1
        else:
            hx = hx + 1
print(len(beenAt))