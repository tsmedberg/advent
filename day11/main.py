from tqdm import tqdm
file = open("day11/input")
lines = file.readlines()
monkeys = []
active = []
numbers = {}
for i in range(len(lines)):
    if "Monkey" in lines[i]:
        items = lines[i+1].split(':')[1].replace(' ','').replace('\n','').split(',')
        operation = lines[i+2].split(':')[1].replace('\n','').split('=')[1]
        test = 'worry % '+lines[i+3].split(':')[1].split(' ')[-1].replace('\n','')+' == 0'
        numbers[test] = {}
        ifTrue = int(lines[i+4].split(':')[1].split(' ')[-1].replace('\n',''))
        ifFalse = int(lines[i+5].split(':')[1].split(' ')[-1].replace('\n',''))
        monkeys.append([items, operation, test, ifTrue, ifFalse])
        active.append(0)
print(monkeys)
for i in tqdm(range(20)):
    for m in range(len(monkeys)):
        items, operation, test, ifTrue, ifFalse = monkeys[m]
        for item in items:
            active[m] = active[m]+1
            worry = int(item)
            worry = eval(operation.replace('old','worry'))
            worry = int(worry/3)
            if not worry in numbers[test]:
                numbers[test][worry] = eval(test)

            if(numbers[test][worry]):

                monkeys[ifTrue][0].append(worry)
            else:
                monkeys[ifFalse][0].append(worry)
        monkeys[m][0]=[]
active.sort()
print(active[-1]*active[-2])
