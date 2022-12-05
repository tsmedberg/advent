import re
file = open('day5/input')
lines = file.readlines()
cargo = [] #first number index, then stack
containerCount = 0 
def vizStack(i):
    text = str(i)+": "
    for x in cargo[i]:
        text = text + str(x)
    print(text)
def viz():
    print('-----BEGIN VIZ-----')
    for i in range(len(cargo)):
        vizStack(i)
    print('------END VIZ------')
def countContainers():
    count = 0
    for stack in cargo:
        count = count + len(stack)
    return count

def deserialize():
    numberIndex = lines.index('\n')-1
    numberMatches = re.finditer('(?:\d)',lines[numberIndex])
    numberIndexes = []
    for num in numberMatches:
        numberIndexes.append(num.start())
    for i in numberIndexes:
        cargo.append([])
    for i in range(numberIndex-1,-1,-1):
        line = lines[i]
        for id,x in enumerate(numberIndexes):
            letter = line[x]
            if not letter.isspace():
                cargo[id].append(letter)
def move(isCrateMover9001=False):
    for ln in range(lines.index('\n')+1,len(lines)):
        if(countContainers() != containerCount):
            raise Exception('uh oh')
        line = lines[ln].replace('\n','')
        split = line.split(' ')
        amount = int(split[1])
        fromStack = int(split[3])-1
        toStack = int(split[5])-1
        if not isCrateMover9001:
            for i in range(amount):
                temp = cargo[fromStack].pop()
                cargo[toStack].append(temp)
        elif isCrateMover9001:
            for container in cargo[fromStack][-amount:]:
                cargo[toStack].append(container)
            cargo[fromStack] = cargo[fromStack][:-amount]
deserialize()
containerCount = countContainers()
move()            
text = ''
for stack in cargo:
    text = text +stack[len(stack)-1]
print(text)
cargo = []
deserialize()
move(isCrateMover9001=True)
text = ''
for stack in cargo:
    text = text +stack[len(stack)-1]
print(text)