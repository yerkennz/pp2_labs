import re

def f(text):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(f("fldkFdlfkdlkfgDFdlkfldfk"))