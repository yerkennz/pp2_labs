n = int(input())
d = {}
for i in range(n):
    s, t = input().split()
    d[s] = d.get(s, 0) + int(t)

x = max(d.values())
d1 = dict(sorted(d.items()))

for i in d1:
    if d1[i] == x:
        print(i, 'is lucky!')
    else:
        print(i, 'has to receive', x-d1[i], 'tenge')