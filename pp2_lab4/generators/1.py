def gen(n):
    for i in range(1, n+1):
        yield i**2

for i in gen(10):
    print(i, end=' ')