import functools
file = open('day13/input')
lines = file.readlines()
correctPackets = []
packets = [[[2]],[[6]]]
def correct(packet1, packet2, dashes=''):
    for e in range(len(packet1)):
        left = packet1[e]
        right = 0
        try:
            right = packet2[e]
        except IndexError:
            return False
        rightIsList = isinstance(left,list)
        leftIsList = isinstance(right,list)
        if rightIsList and not leftIsList:
            right = [right]
            leftIsList = True
        elif leftIsList and not rightIsList:
            left = [left]
            rightIsList = True
        if rightIsList:
            c = correct(left,right,dashes+'- ')
            if c == None:
                if len(left) < len(right):
                    return True
            else:
                return c
        else:
            print(dashes+'Compare '+str(left)+' vs '+str(right))
            if left > right:
                print(dashes+'right is smaller, so input are not in order')
                return False
            elif left < right:
                print(dashes+'left is smaller, so input is in the right order')
                return True
    if len(packet1) == len(packet2):
        return None
    else:
        return True
for i in range(0,len(lines),3):
    packet1 = eval(lines[i])
    packet2 = eval(lines[i+1])
    packets.append(packet1)
    packets.append(packet2)
    print('\nCompare '+str(packet1)+' vs '+str(packet2))
    if correct(packet1,packet2,'- '):
        correctPackets.append(int(i/3)+1)
print('sum of indexes',sum(correctPackets))
packetsSorted = sorted(packets, key=functools.cmp_to_key(correct))
print((packetsSorted.index([[2]])+1)*(packetsSorted.index([[6]])+1))