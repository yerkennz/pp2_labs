def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

s = input().split(' ')
n = int(s[0])
f = int(s[1])
if n <= 500 and is_prime(n) and f%2 == 0:
    print('Good job!')
else:
    print('Try next time!')