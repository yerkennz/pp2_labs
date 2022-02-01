n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(n):
    if a[i] <= 10:
        print('Go to work!')
    elif 10 < a[i] <= 25:
        print('You are weak')
    elif 25 < a[i] <= 45:
        print('Okay, fine')
    elif a[i] > 45:
        print('Burn! Burn! Burn Young!')