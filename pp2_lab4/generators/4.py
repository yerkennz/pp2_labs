def gen(a, b):
    for i in range(a, b+1):
        yield i**2

for i in gen(5, 20):
    print(i, end=' ')