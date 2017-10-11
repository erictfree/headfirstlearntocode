movies = {}
movie = {}

movie['name'] = 'Forbidden Planet'
movie['year'] = 1957
movie['rating'] = '*****'
movie['year'] = 1956

movies['Forbidden Planet'] = movie

movie2 = {'name': 'I Was a Teenage Werewolf',
               'year': 1957, 'rating': '****'}
movie2['rating'] = '***'
movies[movie2['name']] = movie2

movies['Viking Women and the Sea Serpent'] = {'name': 'Viking Women and the Sea Serpent',
                                              'year': 1957,
                                              'rating': '**'}

movies['Vertigo'] =  {'name': 'Vertigo',
                      'year': 1958,
                      'rating': '*****'}

print('Head First Movie Recommendations')
print('--------------------------------')
for name in movies:
    movie = movies[name]
    if len(movie['rating']) >= 4:
        print(movie['name'], '(' + movie['rating'] + ')',  movie['year'])

print('Head First Movie Staff Pick')
print('---------------------------')
movie = movies['I Was a Teenage Werewolf']
print(movie['name'], '(' + movie['rating'] + ')',  movie['year'])

