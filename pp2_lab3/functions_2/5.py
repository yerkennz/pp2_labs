from movies import movies
def cavg(name):
    cnt = 0
    a = 0
    for x in movies:
        if x['category'] == name:
            cnt += x['imdb']
            a += 1
    return cnt/a

print(cavg(input()))