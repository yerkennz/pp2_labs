def pal(s):
    if s == s[::-1]:
        print(s, "is palindrome")
    else:
        print(s, "is not palindrome")

s = input()
pal(s)