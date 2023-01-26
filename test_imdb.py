import imdb

moviesDB = imdb.IMDb()

movies = moviesDB.search_movie('Iron Man')

# for movie in movies:
#     title = movie['title']
#     year = movie['year']
#     print(str(title) + ":" + str(year))

#list movie info
id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
casting = movie['cast']

actor_id = casting[0].getID()
person = moviesDB.get_person(id)

print(title)
print(year)
for actor in casting:
    print(actor)
