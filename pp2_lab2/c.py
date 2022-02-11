n = int(input())
for i in range(n):
    print(i, end=' ')
print(' ')
for i in range(1, n):
    print(i, end=' ')
    for j in range(1, n):
        if i == j:
            print(i*j, end=' ')
        else:
            print(0, end=' ')
    print(' ')