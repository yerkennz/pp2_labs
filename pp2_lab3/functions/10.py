def uni(l):
    x = []
    for y in l:
        if y not in x:
            x.append(y)
    return x

l = input().split()
print(*uni(l))