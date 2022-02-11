def f(c):
    s = c.split('+')
    v = ['ZER', 'ONE', 'TWO', 'THR', 'FOU', 'FIV', 'SIX', 'SEV', 'EIG', 'NIN']
    cnt = 0
    for i in range(len(s)):
        x = '0'
        for j in range(0, len(s[i]), 3):
            x += str(v.index(s[i][j:j+3]))
        cnt += int(x[1:])
    c = str(cnt) 
    for x in c:
        print(v[int(x)], end="") 

f(input())