v = []
while True:
    s = input()
    if s != '0':
        d, m, y = [x for x in s.split()]
        v.append(y + ' ' + m + ' ' + d)
    else:
        break
v.sort()

for x in v:
    print(x[8:], x[5:7], x[:4])
