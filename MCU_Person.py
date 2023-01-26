class Person:

    actor_id = None
    name = None
    sex = None
    media_introduction_year = None
    birth_date = None
    death_date = None
    projected_death_date = None

    def __init__(self):#(self, actor_id, name, sex, media_introduction_year, birth_date, death_date, projected_death_date):
        # self.actor_id = actor_id
        # self.name = name
        # self.sex = sex
        # self.media_introduction_year = media_introduction_year
        # self.birth_date = birth_date
        # self.death_date = death_date
        # self.projected_death_date = projected_death_date
        self.actor_id = None
        self.name = None
        self.sex = None
        self.media_introduction_year = None
        self.birth_date = None
        self.death_date = None
        self.projected_death_date = None

    def calculate_death_date(self):
        import random
        import datetime
        import csv

        #print('kratos', self.birth_date, type(self.birth_date))

        if self.death_date != 'Null':
            # print("This person already has a death date.")
            # print(self.death_date, type(self.death_date))
            return None
        elif self.projected_death_date != None:
            # print("This person already has a projected death date.")
            # print(self.projected_death_date, type(self.projected_death_date))
            return None
        elif self.birth_date == None:
            return None
        else:
            pass


        mdt = "N:\\Data Analysis\\MCU\\Male Death Probability.csv"
        fdt = "N:\\Data Analysis\\MCU\\Female Death Probability.csv"

        male_death_table = open(mdt, 'r')
        female_death_table = open(fdt, 'r')

        if self.sex == 'female':
            reader = csv.reader(female_death_table)
            sex_death_table = female_death_table
        elif self.sex == 'male':
            reader = csv.reader(male_death_table)
            sex_death_table = male_death_table
        else: #default to the male death table for convenience
            reader = csv.reader(male_death_table)
            sex_death_table = male_death_table



        next(reader) #skip the first line of the csv file

        try:
            birth_date_string = self.birth_date
            birth_date_date = datetime.date(*(int(s) for s in birth_date_string.split('-')))
            age = (datetime.date.today().year - birth_date_date.year)
            alive = True
        except:
            birth_date_string = str(datetime.date.today())
            birth_date_date = datetime.date(*(int(s) for s in birth_date_string.split('-')))
            age = (datetime.date.today().year - birth_date_date.year)
            alive = True

        for row in sex_death_table:
            row = row.split(',')
            if age == int(row[0]):  # iterate through the rows
                death_roll = random.randint(1, 100000)  # roll for death
                if death_roll <= int(row[2]):  # if person dies
                    alive = False
                    death_year = birth_date_date.year + age
                    death_month = birth_date_date.month
                    death_day = birth_date_date.day

                    death_date = datetime.date(death_year, death_month, death_day)

                    self.projected_death_date = death_date

                    break
                else:  # person survives
                    age = age + 1  # they get older
            else:
                pass
                # print("wrong age", age, row[0])
        return death_date

    def insert_person(self):
        print("Jello World")