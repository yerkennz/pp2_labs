w = []
for i in range(int(input())):
    d = input().split()
    w.append(d[1])
a = []
k = []
for i in range(int(input())):
    h = input().split()
    a.append(h[1])
    k.append(int(h[2]))

z = 0
for i in a:
    for j in w:
        if k[z] == 0:
            break
        if i == j:
            w.remove(j)
            k[z] -= 1
    z += 1
        
print('Demons left:', len(w))