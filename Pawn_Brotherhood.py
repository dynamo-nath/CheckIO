# find the number of safe pawns


def safe_pawns(positions):
    x = []
    z = []
    pawns = set()
    guards = set()
    safe = 0
    for a in range(0, len(positions)):
        y = (positions.pop())
        i = ((int(y[1]) - 1) * 8) + int(ord(y[0]) - 96)
        x.append(i)
    z = sorted(x, reverse=True)
    # determine pawn squares
    for b in range(0, len(z)):
        pawns.add(z[b])
        #     # determine guard squares
        b1 = z[b] + 9
        b2 = z[b] + 7
        if z[b] % 8 > 1:
            guards.add(b1)
            guards.add(b2)
        elif z[b] % 8 == 1:
            guards.add(b1)
        elif z[b] % 8 == 0:
            guards.add(b2)
    return len(guards & pawns)


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
