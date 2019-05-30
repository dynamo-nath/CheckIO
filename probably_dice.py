from itertools import permutations, product
from random  import randint

counter = 0

# x = list(permutations(range(4), 3))

# total_perms = len(x)
# count_4 = 0

# for i in list(x):
#     if sum(i) == 4:
#         count_4 += 1.0
#         print(f"{i}")

# print(count_4 / total_perms)

a = range(4)
b = range(4)

# input = []
# for j in range(0, 10):
#     input.append(range(1, 11))

# for i in product(*input):
#     if sum(i) == 10:
#         counter += 1


from collections import Counter
from random import randint

def roll(ndice,nsides=6):
    return [randint(1,nsides) for _ in range(ndice)]

def count_it():
    c = Counter(roll(2))
    # return c.most_common(1)[0][1] >= 3
    # print(sum(c))
    return 1 if sum(c) == 3 else None
    # return dict(c)

ntries = 10000000
print (sum(1 for _ in range(ntries) if count_it())/ntries)

# for _ in range(ntries):
# #     print(roll(3))
#     print(count_it())

# print(counter)

# for c in y:
#     if sum(c) == 50:
#         counter += 1.0
#         print(c)

# print(counter / total_perms)
