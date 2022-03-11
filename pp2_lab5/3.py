import re

def f(text):
    patterns = re.compile(r'^[a-z]+_[a-z]+$')
    if re.search(patterns, text):
        return("Yes")
    else:
        return("No")

print(f('abb_bb'))
print(f("abbc"))
print(f("ab_bbbbb"))