import csv
import random
mdt = "N:\\Data Analysis\\MCU\\Male Death Probability.csv"
male_death_table = open(mdt, 'r')
reader = csv.reader(male_death_table)
next(reader)

age = 25 #random.randint(1,100)
alive = True

print(age)
for row in male_death_table:
    row = row.split(',')
    if age == int(row[0]): #iterate through the rows
        death_roll = random.randint(1,100000) #roll for death
        if death_roll <= int(row[2]): #if person dies
            alive = False
            print('You died at age', age, ".  Death Roll:", death_roll, 'vs', row[2])
            break
        else: #person survives
            age = age + 1 #they get older
            #print("Death Roll: ", death_roll, "Vs ", row[2], "You survived to your next birthday:", age)
    else:
        pass
        #print("wrong age", age, row[0])

#for row in male_death_table:
#    row = row.split(',')
#    print(row[0], row[1], row[2])