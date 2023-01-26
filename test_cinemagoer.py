import imdb
import csv
#from MCU_Person import Person as actor
#import test_math_death as death
#import time

ia = imdb.Cinemagoer()
print("Hello World")
mcu_titles = "N:\\Data Analysis\\MCU\\MCU_titles.csv"
movie_text_handle = open(mcu_titles)
file_reader = csv.reader(movie_text_handle)

movie_list = [] # list of movies to search for
movie_dict = {} # movie dictionary that contains retrieved information

for movie in file_reader:
    movie_list.append(movie[0].strip()) #add the csv title to the list of movies
    print("added", movie, "to movie list")


while len(movie_list) > 1: #This gets stuck on Spide-Man: Far From Home when set to 0

    for line in movie_list:

        # retrieve movie title and id from API
        try:
            movies = ia.search_movie(line)
            print(movies[0])
            title = movies[0]['title']
            id = movies[0].movieID
            print(title, id)

            #Here is where the get_casting() function should go

            #check if movie title is already in the movie dictionary
            if title in movie_dict:
                pass
                print(title, "already in dictionary")
            #add current retrieved information to movie dictionary and display new length
            else:
                movie_dict[title] = int(id)
                print("New movie added")

        #This should be the only error
        except:
            pass


    #check to see what movies from the movie list made it into the movie dictionary
    for movie in movie_list:
        if movie in movie_dict:
            movie_list.remove(movie) #remove found movie from movie list
        else:
            pass

print("Final movie dictionary length is", len(movie_dict)) #This should be 30
for movie in movie_dict:
    print(movie, movie_dict[movie])


def get_casting(movie_ID):
    movie = ia.get_movie(movie_ID)  # use IMDB API to get the movie

    cast_list = movie.get('cast')  # set cast list

    cast_member_info = {}

    for cast_member in cast_list:
        person = ia.get_person(cast_member.getID())
        name = cast_member
        try:
            birth_date = person['birth date']
        except:
            birth_date = "Null"
        try:
            death_date = person['death date']
        except:
            death_date = "Null"
        # print(name, birth_date, death_date)
        if birth_date == "Null" or death_date == "Null":
            continue
        else:
            print(name, birth_date, death_date)