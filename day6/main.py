file = open('day6/input')
line = file.readlines()[0]

def isUnique(window):
    unique = True
    for char in window:
        if(window.count(char) > 1):
            unique = False
            break
    return unique
for i in range(4,len(line)):
    if(isUnique(line[i-4:i])):
        print(i)
        break
for i in range(14,len(line)):
    if(isUnique(line[i-14:i])):
        print(i)
        break