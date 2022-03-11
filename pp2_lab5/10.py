import re

def convert(text):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', text.replace('-', ' '))).split()).lower()

print(convert('JavaScript'))