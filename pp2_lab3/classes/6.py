a = [12, 45, 7, 5, 89, 72, 13, 86, 75, 4, 3, 8, 36, 67, 64, 65]

def is_prime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

result = list(filter(is_prime, a))
print(result)