import re

def function(text):
    return re.sub("[ ,.]", ":", text)

print(function('df,dfa,df dfa efb'))
print(function("aa aaafs dsdsdvdvdv ba"))