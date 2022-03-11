import re

def f(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

print(f("NdkflkdlFldkflkdlfKkdlf"))
print(f('KksdksldJlksdlPython'))