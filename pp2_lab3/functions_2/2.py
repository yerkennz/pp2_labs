from movies import movies
hdm = []
def rating():
    for x in movies:
        if x['imdb'] > 5.5:
            hdm.append(x['name'])
        
rating()
for x in hdm:
    print(x, end='\n')

