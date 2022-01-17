#10/31/2021

from datetime import date

todays_date = date.today()
current_year = todays_date.year

#ask the user's birth year and change it to int and make sure he is not born in the future
while True:
    user_birthyear = input ("In which year were you born?")
    try:
        birthyear = int(user_birthyear)
        if birthyear > current_year:  # if the user is born in the future, then ask for input again
            print("Are you kidding? Please try again.")
            continue
        break
    except ValueError:
        print("That's not a year!")    

#calculate the age
age = current_year - birthyear
print("You are now",age,"years old.")

#How many times the user's heart has beaten
#Assumption: A normal heart rate for adults is 80 beats per minute. 
User_heart = 80*60*24*365*age
print("Your heart has beaten",User_heart, "times.")

#How many times a blue whale's heart has beaten
#A study shows that the heart rate of a blue whale can range from 4-8 when diving and 25-37 when swimming to surface. source:https://www.pnas.org/content/116/50/25329
#Assumption: A resting heart rate for blue whales are 6 beats per minute.
Bluewhale_heart = 6*60*24*365*age
print("A blue whale's heart in your age has beaten",Bluewhale_heart, "times.")

#How many times a rabbit's heart has beaten, in million
#The resting heart rate of a rabbit ranges between 140 and 180 beats per minute, according to https://www.medivet.co.uk/pet-care/pet-advice/heart-disease-in-rabbits/.
#Assumption: A resting heart rate for rabbits are 160 beats per minute.
Rabbit_heart = 160*60*24*365*age
Rabbit_heart_inmillion = Rabbit_heart/1000000
print("A rabbit's heart in your age has beaten",Rabbit_heart_inmillion, "million times.")

#How old they are in Venus years
#Assumption: A year on Venus (224.7 days) is shorter than a year on Earth(365.26 days). One Venus year is about 0.615 times the length of an Earth year.
Venus_age = age/0.615
print("Your Venus age is", Venus_age,".")

#How old they are in Neptune years
#Assumption: A year on Neptune(164.79 years) is much longer than a year on Earth. One Venus year is about 164.79 times the length of an Earth year.
Neptune_age = age/164.79
print("Your Neptune age is", Neptune_age, ".")

#Whether they are the same age as you, older or younger, and the difference
My_age = 22
Difference = age - My_age
if Difference > 0:
    print("You are",Difference,"older than me.")
elif Difference < 0:
    print("You are",abs(Difference),"younger than me.")
else:
    print("We are in the same age!") 

#If they were born in an even or odd year
#A number is even if division by 2 gives a remainder of 0.
#If the remainder is 1, it is an odd number
if (birthyear % 2) == 0:
   print("You were born in an even year.")
else:
   print("You were born in an odd year.")

#How many times there has been a president from the Democratic Party in office since they were born
#Which US President was in office when they were born (1960 onward)
#create a dictionary, the keys are the start year and the values are names and parties
Presidents = {1953:['Dwight D. Eisenhower','Republican'],
1961:['John F. Kennedy','Democratic'],
1963:['Lyndon B. Johnson','Democratic'],
1969:['Richard Nixon','Republican'],
1974:['Gerald Ford','Republican'],
1977:['Jimmy Carter','Democratic'],
1981:['Ronald Reagan','Republican'],
1989:['George H. W. Bush','Republican'],
1993:['Bill Clinton','Democratic'],
2001:['George W. Bush','Republican'],
2009:['Barack Obama','Democratic'],
2017:['Donald Trump','Republican'],
2021:['Joe Biden','Democratic']}

#check what range does the birthyear fall
#check from 2021 to 1953. It will stop when birthyear is bigger than the start year of the president
if birthyear < 1960:
    print("Sorry, finding the president service is not available yet for your birthyear.")
else:
    for y in sorted(Presidents.keys(), reverse=True):
        if birthyear >= y:
            break
    president_year = y
    president = Presidents[y][0]
    print("President",president,"was in office when you were born.")

 #check from the birthyear to 2021. If the president party is democratic, count once.
    Democratic_number = 0
    for y in sorted(Presidents.keys()):
        if president_year <= y and Presidents[y][1] == 'Democratic':
            Democratic_number = Democratic_number +1
    print("There has been",Democratic_number,"Democratic presidents since you were born.")