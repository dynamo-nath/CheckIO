def testing(data):
    n = set.union(*data)
    n1 = set()
    for x in range(0, len(data)):
        if len(n1) == 0:
            n1 = data[0]
        else:
            if len(n1.intersection(data[x])) > 0:
                n1 = n1.union(data[x])
    print(n1)



a = [{'a', 'c'}, {'c', 'e'}, {'a', 'd'}, {'e', 'x'}, {'x', 'y'}]
testing(a)