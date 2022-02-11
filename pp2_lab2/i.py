n = int(input())
v = []
d = []
for i in range(n):
    s = input().split()
    if int(s[0]) == 1:
        v.append(s[1])
    elif int(s[0]) == 2:
        if len(v) != 0:
            d.append(v[0])
            v.pop(0)
for x in d:
    print(x, end=' ')