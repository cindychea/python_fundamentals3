# Create Lists
fav_colors = ['red', 'blue', 'purple', 'seafoam']
cousin_ages = [31, 33, 25, 35, 22]
flipped_heads = [True, True, False, False, True]
fav_artists = ['Travis', 'Bazzi', 'Tinashe']

# Create Dictionaries
words_defs = {
    'blossom': 'the state of flowering',
    'flower': 'the blossom of a plant',
    'stem': 'the stalk that supports a lead, flower, or fruit'
}
movie_years = {
    'Hitch': 2005,
    'Over the Hedge': 2006,
    'Kung Fu Panda': 2008
}
cities_pop = {
    'Toronto': 2.93,
    'Sydney': 4.627,
    'Milan': 1.352
}
family_ages = {
    'Amy': 22,
    'Ida': 31,
    'Filly': 35,
    'Huoi': 33
}

# EXERCISE 1
# print(flipped_heads)

# print(fav_colors[0])

# print(sorted(cousin_ages))

# cousin_ages.append('0')
# print(cousin_ages)

# print(movie_years['Hitch'])

# EXERCISE 2
# print(fav_colors[-1])

# cities_pop['Paris'] = 2.141
# print(cities_pop)

# list.reverse(flipped_heads)
# print(flipped_heads)

# print(cities_pop['Milan'])

# for artist in fav_artists:
#     print("I think {} is great.".format(artist))

# EXERCISE 3
# print(fav_artists[0:2])

# for movie, year in movie_years.items():
#     print("{} came out in {}.".format(movie,year))

# print(list(reversed(sorted(cousin_ages))))

# movie_years['Beauty and the Beast'] = '1991', '2017'
# print(movie_years)

# EXERCISE 4
# under_thirty = list(filter(lambda number: number < 30, cousin_ages))
# print(under_thirty)

# cousin_ages.sort()
# print(cousin_ages[-1])

# print(flipped_heads.count(True))

# fav_artists.pop(1)
# print(fav_artists)

# cities_pop['Sydney']=4.900
# print(cities_pop)

# EXERCISE 5
# print(sum(cities_pop.values()))

# for names,ages in family_ages.items():
#     if ages > 30:
#         print("{} is old.".format(names))
#     else:
#         print("{} is young.".format(names))

# print(fav_colors[-2:])

# for ages in cousin_ages:
#     print(ages + 1)

# fav_colors.append('coral')
# fav_colors.append('lime green')
# print(fav_colors)

# EXERCISE 6
listed_movies = {
    1999: ['The Matrix', 'Star Wars: Episode 1', 'The Mummy'],
    2009: ['Avatar','Star Trek', 'District 9'],
    2019: ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Episode 9']
}
phone_buttons = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['*', 0, '#']
]
country_info = [
    {
        'Country':'Peru',
        'Continent': 'South America',
        'Island': False
    },
    {
        'Country':'New Zealand',
        'Continent': 'Australia',
        'Island': True
    },
    {
        'Country': 'Chile',
        'Continent': 'South America',
        'Island': False
    }
]
