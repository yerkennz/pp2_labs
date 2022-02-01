n = input()
s = 0
j = 0
for i in range(len(n)-1, -1, -1):
    s += int(n[i])*2**j
    j += 1
print(s)