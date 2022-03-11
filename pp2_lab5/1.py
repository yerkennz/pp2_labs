import re

def f(text):
    patterns = re.compile(r'^a(b*)$')
    if re.search(patterns, text):
        return("Yes")
    else:
        return("No")

print(f('abbbb'))
print(f("abbc"))

