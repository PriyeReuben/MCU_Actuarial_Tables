import csv
import imdb
import datetime

from MCU_Person import Person
from MCU_Sex import Sex
from MCU_cinemagoer import Movie_info
from MCU_Tables import Database

cast_list = []
actor_entry = []
movie_dict = {}
ia = imdb.Cinemagoer()
current_movie = Movie_info()
current_person = Person()
database = Database()
#database.create_table()


mcu_titles = "N:\\Data Analysis\\MCU\\MCU_titles.csv"
movie_text_handle = open(mcu_titles)
file_reader = csv.reader(movie_text_handle)

for movie in file_reader:
    title = movie[0]
    movie_id = movie[1]
    current_movie.movie_id = movie_id
    cast_list = current_movie.get_cast_list(movie_id)

    for actor in cast_list:
        name = actor
        actor = repr(actor).split()
        actor_id = actor[1][3:10]
        try:
            actor_info = ia.get_person(actor_id)
        except:
            continue

        try:
            current_person.actor_id = actor_id
            current_person.name = str(name)
            current_person.sex = None
            current_person.media_introduction_year = None
            current_person.projected_death_date = None
        except:
            print("something went wrong")

        try:
            current_person.birth_date = actor_info['birth date']

            if actor_info['birth date'][5:7] == '00':
                continue
            elif actor_info['birth date'][8:10] == '00':
                continue
            elif actor_info['birth date'][0:4] == '0':
                continue
            else:
                pass

        except:
            #current_person.birth_date = str(datetime.date.today())#rather than putting in someone born today, just skip
            continue

        try:
            #print(current_person.birth_date, type(current_person.birth_date))
            current_person.death_date = actor_info['death date']
        except:
            current_person.death_date = 'Null' #datetime.date.today()





        #print('passed PPD')

        #get sex
        full_name = current_person.name
        first_name = full_name.split()[0]
        current_sex = Sex(first_name)
        current_person.sex = current_sex.get_sex()

        #get PPD
        current_person.projected_death_date = current_person.calculate_death_date()
        #print('hecatonchires', current_person.projected_death_date)

        # print(current_person.actor_id, current_person.name, current_person.sex, current_person.birth_date,
        #       current_person.death_date, current_person.projected_death_date, current_movie.movie_id,
        #       current_movie.release_year)

        actor_entry.append(current_person.actor_id)
        actor_entry.append(current_movie.movie_id)
        actor_entry.append(current_person.name)
        actor_entry.append(current_person.sex)
        actor_entry.append(current_person.birth_date)
        actor_entry.append(current_person.death_date)
        actor_entry.append(current_person.projected_death_date)
        actor_entry.append(current_movie.release_year)

        print(actor_entry)
        database.insert_one(actor_entry)
        actor_entry.clear()

    cast_list.append(actor_entry)

    cast_list.clear()


database.remove_values()
database.show_all()


        #print(name, actor_id)




# movie_dict = {'Iron Man':'371746', 'The Incredible Hulk':'80080'}
# #this_person = Person()
# this_person = Person('123456', 'Reginald Smith', None, '2008', '1999-05-25', None, None)
# first_name = this_person.name.split()[0]
# this_sex = Sex(first_name)
# print(this_sex.get_sex())


