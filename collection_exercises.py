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

# Exercise 1
# print(flipped_heads)
# print(fav_colors[0])
# print(sorted(cousin_ages))
# cousin_ages.append('0')
# print(cousin_ages)
# print(movie_years['Hitch'])

#Exercise 2
print(fav_colors[-1])

cities_pop['Paris'] = 2.141
print(cities_pop)

list.reverse(flipped_heads)
print(flipped_heads)

print(cities_pop['Milan'])

for artist in fav_artists:
    print("I think {} is great.".format(artist))
