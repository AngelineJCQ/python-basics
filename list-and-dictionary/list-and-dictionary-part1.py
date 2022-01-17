#11/01/21

#Lists
from statistics import mean, median

#Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
list1 = [22, 90, 0, -10, 3, 22, 48]
#Display the number of elements in the list.
print(list1)
#Display the 4th element of this list.
print(list1[3])
#Display the sum of the 2nd and 4th element of the list.
print(list1[3]+list1[1])
#Display the 2nd-largest value in the list.
list_sort = sorted(list1)
print(list_sort[-2])
#Display the last element of the original unsorted list
print(list1[-1])
#Display the sum of all of the numbers divided by two.
list_divide = []
for n in list1:
    list_divide.append(n/2)
print(sum(list_divide))
#Print whether the median or the mean of the numbers is higher
a = mean(list1)
b = median(list1)
if a > b:
    print("The average of the list is higher than the median.")
elif a == b:
    print("The average of the list eaquals to the median.")
else:
    print("The median of the list is higher than the average.")

#Dictionaries
movie = {'title': 'The Dark Knight',
'year':2008,
'director': 'Christopher Nolan'
}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
#add keys to the movie dictionary for budget and revenue
#The budget of that movie is $185 million, and the box office is $1.005 billion.
movie['budget'] = 185000000
movie['revenue'] = 1005000000
#another way of doing it
#movie.update(budget = 185000000, revenue =1005000000)
#print out the difference between the two
revenue = movie['revenue']
budget = movie['budget']
profit = revenue - budget
print("The profit of this movie is", profit)

#To decide whether it's a good investment
if profit < 0:
    print( "That was a bad investment.")
elif revenue/budget > 5:
    print("That was a great investment." )
else:
    print("That was an okay investment.")

#Create a NYC population dictionary
population_nyc = {'Manhattan': 1.6,
'Brooklyn': 2.6,
'Bronx': 1.4,
'Queens': 2.3,
'Staten Island': 0.47
}
#Display the population of Brooklyn.
print("The population in Brooklyn is",population_nyc['Brooklyn'],"millions.")

#Display the combined population of all five boroughs.
sum_nyc = 0
for b in population_nyc:
    sum_nyc = sum_nyc + population_nyc[b]
print("The combined population of all five boroughs is",sum_nyc,"millions.")

#Display what percent of NYC's population lives in Manhattan.
percentage_manhattan = population_nyc['Manhattan']/sum_nyc
#format the percentage in a real % way
format_per = '%.2f%%'%(percentage_manhattan*100)
print(format_per,"of NYC's population lives in Manhattan.")
