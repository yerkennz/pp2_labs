import re

def f(text):
    patterns = re.compile(r'^a(b.{3,4})$')
    if re.search(patterns, text):
        return("Yes")
    else:
        return("No")

print(f('abbbb'))
print(f("abbc"))
print(f("abbbbbb"))