n, c = int(input()), input()
if c == 'k':
    e = int(input())
    x = n/1024
    print(round(x, e))
if c == 'b':
    print(n*1024)