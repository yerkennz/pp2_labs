from movies import movies
def rating(movie):
    for x in movies:
        if x['name'] == movie and x['imdb'] > 5.5:
            return True
    return False

print(rating(input()))
