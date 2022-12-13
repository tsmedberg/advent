file = open("day10/input")
lines = file.readlines()
x = 1
ops = [0]
sum = 0
screen = ""
    
for line in lines:
    line = line.replace('\n','').split(' ')
    op = line[0]
    ops.append(0)
    if op == 'addx':
        ops.append(int(line[1]))
for i in range(len(ops)):
    x = x+ops[i]
    if i in range(19,220,40):
        sum = sum + x*(i+1)
    y = i
    while y > 39:
        y = y - 40
    if y in range (x-1,x+2,1):
        screen = screen + "#"
    else:
        screen = screen + "."
for i in range(6):
    print(screen[i*40:i*40+40])
print(len(ops))
print(sum)