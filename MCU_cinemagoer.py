import imdb
import csv
mcu_titles = "N:\\Data Analysis\\MCU\\MCU_titles.csv"

class Movie_info:


    movie_id = None
    title = None
    release_year = None
    additions = None #IDK about this


    def __init__(self):
        self.movie_id = None
        self.title = None
        self.release_year = None
        self.additions = None
        self.cast_list = []
        self.ia = imdb.Cinemagoer()

        movie_text_handle = open(mcu_titles)
        file_reader = csv.reader(movie_text_handle)
        movie_list = []  # list of movies to search for
        movie_dict = {}  # movie dictionary that contains retrieved information

    def get_cast_list(self, movie_id):
        movie = self.ia.get_movie(str(movie_id))

        self.movie_id = movie_id
        self.title = movie.get('title')
        self.release_year = movie.get('year')
        self.cast_list = movie.get('cast')

        return self.cast_list



# a = Movie_info()
# iron_man_cast = a.get_movie('371746')
#
#
# for value in a.cast_list:
#     value = repr(value).split()
#     actor_id = value[1][3:10]
#
#     print(actor_id,value)