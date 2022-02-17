def rev(n):
    n.reverse()
    return n

n = input().split()
print(*rev(n))
