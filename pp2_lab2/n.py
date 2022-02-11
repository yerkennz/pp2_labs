numbers = []
while True:
    s = int(input())
    if s != 0:
        numbers.append(s)
    else:
        break
if len(numbers)%2 == 0:
    for i in range(len(numbers)//2):
        print(numbers[i]+numbers[len(numbers)-i-1], end=' ')
else:
    for i in range(len(numbers)//2):
        print(numbers[i]+numbers[len(numbers)-i-1], end=' ')
    print(numbers[len(numbers)//2])
