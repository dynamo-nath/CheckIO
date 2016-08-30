import math as m


def checkio(s1=None, s2=None, s3=None):
    if type(s1) is list:
        t1 = s1
        s1 = t1[0]
        s2 = t1[1]
        s3 = t1[2]

    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        return [0, 0, 0]
    elif s1 > 1000 or s2 > 1000 or s3 > 1000:
        return [0, 0, 0]
    elif s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
        return [0, 0, 0]
    elif s1 == s2 == s3:
        a1 = 60
        a2 = 60
        a3 = 60
    else:
        a1 = m.degrees(m.acos(((s2 ** 2) + (s3 ** 2) - (s1 ** 2)) / (2 * s2 * s3)))
        a2 = m.degrees(m.acos(((s3 ** 2) + (s1 ** 2) - (s2 ** 2)) / (2 * s1 * s3)))
        a3 = 180 - round(a1) - round(a2)

    return sorted([round(a1), round(a2), round(a3)])


a = [2, 2, 5]
print(checkio(a))
