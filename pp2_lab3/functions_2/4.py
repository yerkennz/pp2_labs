from movies import movies
def avg(n):
    cnt = 0
    for x in n:
        for m in movies:
            if x == m['name']:
                cnt += m['imdb']
    return cnt/len(n)

n = ['Joking muck', 'Detective', 'Colonia', 'Usual Suspects', 'We Two']
 
print(avg(n))