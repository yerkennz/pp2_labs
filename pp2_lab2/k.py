s = (input().split())
d = set(s)
print(len(d))
v = []
for x in d:
    if 64 < ord(x[-1]) < 91 or 96 < ord(x[-1]) < 123:
        v.append(x)
    else:
        v.append(x[:-1])
v.sort()
for x in v:
    print(x)