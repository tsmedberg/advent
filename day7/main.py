file = open('day7/input')
lines = file.readlines()
fs = {}
cd = ''
for line in lines:
    if(line[0] == '$'): #is command
        line = line.replace('\n','')
        line = line[2:]
        splits = line.split(' ')
        cmd = splits[0]
        arg = None
        if len(splits) > 1:
            arg = splits[1]
        if(cmd == 'cd'):
            if arg == '..':
                cd = '/'.join(cd.split('/')[:-2]) +'/'
            else:
                cd = cd + arg
                if(cd[-1:]) != '/':
                    cd = cd + '/'
                fs[cd]=[]
            print(line,'>',cd)
    else:
        listing = line.replace('\n','').split(' ')
        size = listing[0]
        if size.isnumeric():
            #we have file
            fs[cd].append([listing[1],int(size)])
def calcutateDirSize(dir,dash='-'):
    size = 0
    for path in fs.keys():
        if path.startswith(dir):
            for file in fs[path]:
                size = size + file[1]
    #print(dash[:-1],size)
    return size

totalSize = 0
bigEnoughToDelete = []
spaceNeeded = 0
for path in fs.keys():
    s = calcutateDirSize(path)
    if(path == '/'):
        print('root size is',s)
        spaceNeeded =30000000 - (70000000 - s)
    if s <= 100000:
        totalSize = totalSize + s
    if(s > spaceNeeded):
        bigEnoughToDelete.append(s)
bigEnoughToDelete.sort()
print(totalSize)
print(bigEnoughToDelete[0])
