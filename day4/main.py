file = open('day4/input')
lines = file.readlines()

fullyContains = 0
anyOverlap = 0
def contains(parent,child):
    [ps, pe] = parent.split('-')
    [cs, ce] = child.split('-')
    ps = int(ps)
    pe = int(pe)
    cs = int(cs)
    ce = int(ce)
    return cs >= ps and ce <= pe
def overlap(parent,child):
    [ps, pe] = parent.split('-')
    [cs, ce] = child.split('-')
    ps = int(ps)
    pe = int(pe)
    cs = int(cs)
    ce = int(ce)
    return numberIn(cs,ps,pe) or numberIn(ce,ps,pe)

def numberIn(test,start,end):
    return start <= test <= end

for line in lines:
    [area1, area2] = line.split(',')
    c = contains(area1,area2) or contains(area2,area1)
    o = overlap(area1,area2) or overlap(area2,area1)
    if c:
        print(area1,area2)
        fullyContains = fullyContains + 1
    if o:
        print(area1, area2)
        anyOverlap = anyOverlap + 1
print('Fully contains',fullyContains)
print('Any overlap',anyOverlap)