s = input().split()
if len(s) == 1:
    s1 = input()
    n, x = int(s[0]), int(s1)
else:
    n, x = [int(x) for x in s]

y = x
for i in range(1, n):
    x ^= y + 2*i
print(x)