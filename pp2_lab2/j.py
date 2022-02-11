n = int(input())
v = [input() for i in range(n)]
d = []

def strpass(v):
    for i in range(len(v)):
        a, b, c = 0, 0, 0
        for j in range(len(v[i])):
            if 47 < ord(v[i][j]) < 58:
                a += 1
            if 64 < ord(v[i][j]) < 91:
                b += 1
            if 96 < ord(v[i][j]) < 123:
                c += 1
        if a > 0 and b > 0 and c > 0:
            d.append(v[i])        
    
strpass(v)
d = sorted(list(set(d)))
print(len(d))
for x in d:
    print(x)