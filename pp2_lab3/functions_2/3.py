from movies import movies
ct = []
def category(name):
    for x in movies:
        if x["category"] == name:
            ct.append(x['name'])

category(input())
for x in ct:
    print(x, end="\n")