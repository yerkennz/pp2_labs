n = int(input())
v = []
for i in range(n):
    c = input()
    if '@gmail.com' in c:
        c.replace('@gmail.com','')
        v.append(c[:-10])
for i in range(len(v)):
    print(v[i])