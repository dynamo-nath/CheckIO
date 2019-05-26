
def most_wanted(myString):
    z = []
    b = myString.lower()
    for a in range(1, 27):
        z.append(b.count(chr(96+a)))
    return chr(96+z.index(max(z))+1)

print(most_wanted('AAaooo!!!!'))