n = int(input())
a = input().split(' ')
numbers = [int(x) for x in a]
c = max(numbers)
b = numbers.remove(c)
print(c*max(numbers))