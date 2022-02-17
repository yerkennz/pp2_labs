from itertools import permutations
def nexper(n):
    a = permutations(n)
    for i in list(a):
        print(*i, sep='')

n = input()
nexper(n)
