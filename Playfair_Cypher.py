import re


def encode(message, keyword):
    # clans input message and calls grid function
    grid = (make_grid(keyword))
    # message
    l = message.lower()
    a = ''
    a1 = ''
    # filter out symbols and spaces
    for x in range(len(l)):
        x1 = re.findall('[a-z0-9]', l[x])
        if len(x1) > 0:
            a += x1[0]
    # print(a)
    digraph = encode1(a1, a)


def encode1(a1, b):
    b1 = ''
    print(len(a1))
    if len(b) == 0:
        print('1')
        return a1
    elif len(b) == 1 and len(a1) % 2 == 0:
        if b[0] == 'x':
            print('2:', a1 + b[0] + 'z')
            return a1
        else:
            print('2.5:', a1 + b[0] + 'x')
            return a1
    # is len(a1) % 2 ever not 0?
    elif len(b) == 1 and len(a1) % 2 != 0:
        if b[0] == 'x':
            print('3')
            return a1
        else:
            print('4')
            return a1

    if b[0] != b[1]:
        a1 += b[0] + b[1]
        b1 = b[2:]
    elif b[0] == b[1] and b[0] != 'x':
        a1 += b[0] + 'x'
        b1 = b[1:]
    elif b[0] == b[1] and b[0] == 'x':
        a1 += b[0] + 'z'
        b1 = b[1:]
    # print(a1)
    return encode1(a1, b1)


def decode(message, keyword):
    pass


def make_grid(keyword):
    # create table
    r1 = []
    raw = 'abcdefghijklmnopqrstuvwxyz0123456789'
    ts = ''
    for t in range(0, len(keyword)):
        if keyword[t] not in ts:
            ts += keyword[t]
    for t in range(0, len(raw)):
        if raw[t] not in ts:
            ts += raw[t]
    for s in range(0, 6):
        ts1 = ''
        for s1 in range(0, 6):
            ts1 += ts[s * 6 + s1]
        r1.append(ts1)
    return r1


encode('Hello World!', 'checkio101')
