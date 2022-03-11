import re

def function(text):
    patterns = re.compile(r'a.*?b$')
    if re.search(patterns, text):
        return("match")
    else:
        return "not match"

print(function('dfdfadfdfaefb'))
print(function("aaaaafsdsdsdvdvdvba"))