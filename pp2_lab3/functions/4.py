p = []
def filter_prime(n):
    for x in n:
        flag = True
        for i in range(2, x):
            if x%i == 0:
                flag = False
                break
        if flag == True and x != 1:
            p.append(x)

n = [int(x) for x in input().split()]
filter_prime(n)
print(*set(p))