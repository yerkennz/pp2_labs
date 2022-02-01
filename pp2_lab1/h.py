s = input()
c = input()
v = []
for i in range(len(s)):
    if c == s[i]:
        v.append(i)
if len(v) == 1:
    print(v[0])
elif len(v) >= 2:
    print(v[0], v[-1], sep=' ')