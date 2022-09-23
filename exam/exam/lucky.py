def lucky(startNumber, endNumber, numberOfRemoves):
    l = generate_list(startNumber, endNumber)
    pos = 0
    prev = l[pos]
    if numberOfRemoves > 0:
        remove(l, prev)
        pos += 1
        prev = l[pos]
    numberOfRemoves -= 1
    print(l)

    while numberOfRemoves > 0 and len(l) >= prev:
        remove(l, prev)
        if prev == l[pos]:
            pos += 1
        prev = l[pos]
        print(l)
        numberOfRemoves -= 1

    return l

def generate_list(startNumber, endNumber):
    l = []
    while startNumber <= endNumber:
        l.append(startNumber)
        startNumber += 1
    return l

def remove(l, value):
    if value != 1:
        num = value
        rounds = 0
        while num - rounds <= len(l):
            del l[num - 1 - rounds]
            rounds += 1
            num += value

lucky(1, 19, 4)
