import random
print("Hello! What is your name?")
name = input()
print("Well,", name, "I am thinking of a number between 1 and 20.")
print("Take a guess.")
num = int(input())
r = random.randrange(1, 20)
cnt = 1
while num != r:
    if num < r:
        print("Your guess is too low.")
    elif num > r:
        print("Your guess is too high.")
    print("Take a guess.")
    num = int(input())
    cnt += 1

print("Good job,", name,"! You guessed my number in", cnt ,"guesses!")
