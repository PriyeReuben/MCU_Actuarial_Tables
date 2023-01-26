from imdb import Cinemagoer
# create an instance of the IMDb class
ia = Cinemagoer()

# search for a person name
this_movie = ia.get_movie('371746')
this_person = ia.search_movie("Thor")

print(this_movie)
print(this_person)


# for person in this_person:
#     print(person.personID, person['name'])