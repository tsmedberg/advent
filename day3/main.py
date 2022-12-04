file = open('day3/input')
lines = file.readlines()
sumBoth = 0
sumThree = 0
def inBoth(c1,c2):
    both = None
    for char in c1:
        if char in c2:
            both = char
            break
    return both
def inThree(l1,l2,l3):
    three = None
    for char in l1:
        if char in l2 and char in l3:
            three = char
            break
    return three

def priority(char):
    prio = None
    if(char.islower()):
        prio = ord(char)-96
    else:
        prio = ord(char)-38
    return prio

for line in lines:
    line = line.replace('\n','')
    half = int(len(line)/2)
    c1 = line[:half]
    c2 = line[half:]
    sumBoth = sumBoth + priority(inBoth(c1,c2))
i = 0
while i+2 <= len(lines):
    l1 = lines[i]
    l2 = lines[i+1]
    l3 = lines[i+2]
    sumThree = sumThree + priority(inThree(l1,l2,l3))
    i = i+3
print('compartments',sumBoth)
print('badge',sumThree)