from ast import pattern
import re

def convert(text):
    return ''.join(x.capitalize()  for x in text.split('_'))

print(convert("to_dfd_sdf_dfdf"))
print(convert("to_dddsdsd_sd"))
print(convert("to_dfd"))
print(convert("to_dfd_sdf_dfdf"))