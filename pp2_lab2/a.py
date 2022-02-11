n = [int(x) for x in input().split()]

def f(n):
    cur = 0
    for i in range(len(n)):
        if i > cur:
            return False
        if n[i] + i > cur:
            cur = n[i]+i
        if cur >= len(n)-1:
            return True


if (f(n)):
    print(1)
else:
    print(0)