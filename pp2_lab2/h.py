x, y = [int(x) for x in input().split()]
n = int(input())
d = []

def point(d):
    return ((d[0]-x)**2 + (d[1]-y)**2)**0.5 

for i in range(n):
    s = [int(x) for x in input().split()]
    d.append(s)

d.sort(key = point)

for i in range(n):
    for j in range(2):
        print(d[i][j], end=" ")
    print()
