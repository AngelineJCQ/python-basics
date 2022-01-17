#11/06/21

#PART ONE: Pokemon API

#What is the URL to the documentation?
#https://pokeapi.co/docs/v2

#What pokemon has the ID of 55?
import requests
response1 = requests.get("https://pokeapi.co/api/v2/pokemon/55/")
pokemon55 = response1.json()
print("The pokemon with ID 55 is", pokemon55['name']+".")
#How tall is that pokemon?
print(pokemon55['name'], "is", pokemon55['height'], "decimetres tall.")

#How many versions of Pokemon games have been released?
response2 = requests.get("https://pokeapi.co/api/v2/version/")
version = response2.json()
print("There are", version['count'], "versions of Pokemon games.")

#Another way
'''
response2 = requests.get("https://pokeapi.co/api/v2/version/")
version = response2.json()
version_number = len(version['results'])
print(version_number)
'''
#You can see next":"https://pokeapi.co/api/v2/version/?offset=20&limit=14"
#limit means the result is not the entire versions
#so change the url "https://pokeapi.co/api/v2/version/?offset=20&limit=1000"
response2 = requests.get("https://pokeapi.co/api/v2/version/?limit=1000")
version = response2.json()
version_number = len(version['results'])
print(version_number)

#Print out the name of every electric-type pokemon.
response3 = requests.get("https://pokeapi.co/api/v2/type/electric/")
electric = response3.json()
electric_pokemons = electric["pokemon"]
electric_pokemon_name_url = [e_p['pokemon'] for e_p in electric_pokemons]
electric_pokemon_name = [pname['name'] for pname in electric_pokemon_name_url]
print(electric_pokemon_name)
#What are electric-type Pokemon called in the Korean version of the game?
languages = electric["names"]
for l in languages:
    if l["language"]["name"] == 'ko':
        print("The electric-type Pokemon in the Korean version of the game is called", l['name'])
#Who has a higher speed stat, Eevee or Pikachu?
response4 = requests.get("https://pokeapi.co/api/v2/pokemon/eevee/")
eevee = response4.json()
eevee_stats = eevee["stats"]
for es in eevee_stats:
    if es["stat"]["name"] == "speed":
        eevee_speed = es["base_stat"]
response5 = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
pikachu = response5.json()
pikachu_stats = pikachu["stats"]
for ps in pikachu_stats:
    if ps["stat"]["name"] == "speed":
        pikachu_speed = ps["base_stat"]
if pikachu_speed > eevee_speed:
    print("Pikachu has a higher speed stat than Eevee.")
elif pikachu_speed == eevee_speed:
    print("Pikachu has the same speed stat as Eevee.")
else:
    print("Eevee has a higher speed stat than Pikachu.")

#PART TWO: Weather API

#What is the URL to the documentation?
#http://www.weatherapi.com/docs/

#Make a request for the current weather where you are born, or somewhere you've lived.
response6 = requests.get("http://api.weatherapi.com/v1/current.json?key= &q=Ningbo")
ningbo_wheather = response6.json()

#Print out the country this location is in.
country = ningbo_wheather["location"]["country"]
print("Ningbo is in", country)
#Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.
ningbo_temp_c = ningbo_wheather["current"]["temp_c"]
ningbo_feelslike_c = ningbo_wheather["current"]["feelslike_c"]
difference = ningbo_feelslike_c - ningbo_temp_c
if ningbo_feelslike_c > ningbo_temp_c:
    print("It feels", difference, "Celsius degrees warmer.")
else:
    print("It feels", abs(difference), "Celsius degrees colder.")

#What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
response7 = requests.get("http://api.weatherapi.com/v1/current.json?key= &q=LHR")
heathrow_wheather = response7.json()
heathrow_temp_c = heathrow_wheather["current"]["temp_c"]
print("The current temperature at Heathrow International Airport is",heathrow_temp_c, "degree Celsius.")

#What URL would I use to request a 3-day forecast at Heathrow?
response8 = requests.get("http://api.weatherapi.com/v1/forecast.json?key= &q=LHR&days=3")
heathrow_forcast = response8.json()

#Print the date of each of the 3 days you're getting a forecast for.
forcast_dates = heathrow_forcast["forecast"]["forecastday"]
for day in forcast_dates:
    print(day["date"])
    #Print the maximum temperature of each of the days.
    print(day["day"]["maxtemp_c"])

#Print the day with the highest maximum temperature.
keys = [day["date"] for day in forcast_dates]
values = [day["day"]["maxtemp_c"] for day in forcast_dates]
forecast = dict(zip(keys,values))
day_highest = []
for key, value in forecast.items():
    if value == max(forecast.values()):
        max_key = key
        day_highest.append(key)
print(day_highest)
