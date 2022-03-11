import re

def f(text):
    patterns = re.compile(r'[A-Z]+[a-z]+$')
    if re.search(patterns, text):
        return("Yes")
    else:
        return("No")

print(f('Abbbb'))
print(f("aDbc"))
print(f("abbbbbb"))