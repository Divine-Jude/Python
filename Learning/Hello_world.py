from math import sqrt

print("Hello Python world!")

message = "Hello Python crash course world!"
print(message)

character_name = "Divine"
character_age = "24"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")

character_name = "Jude"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

print('I told my friend, "Python is my favorite language!"')
print("the language 'python' is named after monty python, not the snake")
print("one of python's strengths is its diverse and supportive community")

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.upper()}!"
print(message)

print("Python")
print("\tpython")
print("languages:\n\tpython\n\tC\n\tjavascript")

favorite = "one of python's strength."
print(favorite)

print(sqrt(36))

# LISTS
bicycles = ['trek', 'cannon-dale', 'red line', 'specialized']
print(bicycles[0])
bicycles = ['trek', 'cannon-dale', 'red line', 'specialized']
print(bicycles[-2])

# using f-string
bicycles = ['trek', 'cannon-dale', 'red line', 'specialized']
message = f"My first bicycle was a {bicycles[0]} yes!"
print(message)

# changing elements
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[0] = "Qlik"
print(motorcycles[0])

# adding element to lists
motorcycles = ['honda', 'yamaha', 'suzuki', 'ferrari']
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# inserting new element to any position
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducat')
print(motorcycles)

# removing elements using del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# using remove element
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducat']
# motorcycles.remove('ducat')
# print(motorcycles)
too_expensive = 'ducat'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# sorting a list
car = ['bmw', 'audi', 'toyota', 'subaru']
car.sort()
print(car)
car.sort(reverse=True)
print(car)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print(len(cars))

# using loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# represents a single item from the list
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"i can't to see your next trick, {magician.title()}. \n")
print("Thank you, everyone. That was a great magic show!\n")

# Range
for value in range(1, 6):
    print(value)
    
# using range to make list
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# using for loop
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# also
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:5:2])

# looping through a slice
players = ['durant', 'leBron', 'jordan', 'giannis', 'kobe']
for player in players[:3]:
    print(player.title())
 
# copying a list
my_foods = ['pizza', 'favail', 'carrot cake']
friend_foods = my_foods[0:1]
my_foods.insert(1, 'ice cream')
print(f"\nMy favorite foods are:")
print(my_foods)
friend_foods.append('butter')
print("\nMy friend's favorite foods are:")
print(friend_foods)

# TUPLES
dimension = (200, 50)
print(dimension[0])
print(dimension[1])
my_t = (3,)
print(my_t[0])

# looping through a tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    
# writing over tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 50)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# if statement
cars = ['audi', 'Bmw', 'subaru', 'toyota']
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())
new_cars = ['BMW']
for new_car in new_cars:
    if new_car == 'bmw':
        print(new_car.upper())
    else:
        print(new_car.title())
        
# Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("hold the anchovies!")
    
# numbers comparison
answer = 17
if answer != 42:
    print("The answer is not correct. please try again")
age = 19
if age < 21:
    print("TRUE")
else:
    print("False")
    
# Using AND to Check Multiple Conditions
age_0 = 22
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print("True")
else:
    print("False")
    
# using OR
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print("True")
else:
    print("False")
    
# Checking Whether a Value Is Not in a List using NOT
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have to registered to vote?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# Testing for two possible conditions
# consider an amusement park that charges different rates for different age groups:
# • Admission for anyone under age 4 is free.
# • Admission for anyone between the ages of 4 and 18 is $25.
# • Admission for anyone ages 18 or older is $40.
# How can we use an if statement to determine a person’s admission rate?
# The following code tests for the age group of a person and then prints an admission price message:
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age <= 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
age = 12
if age < 4:
    price = 0
elif age > 18:
    price = 25
elif age < 65:
    price = 20
else:
    price = 40
print(f"Your admission cost is ${price}.")

ages = 12
if ages < 4:
    price = 0
elif ages < 18:
    price = 25
elif ages < 65:
    price = 40
elif ages >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("adding mushrooms")
if 'pepperoni' in requested_topping:
    print("adding pepperoni")
if 'extra cheese' in requested_topping:
    print("\nadding extra cheese")
    
# Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("\nSorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

# Checking That a List Is Not Empty
toppings = []
if toppings:
    for topping in toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")
    
# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
list_toppings = ['mushrooms', 'french fries', 'extra cheese']
for list_topping in list_toppings:
    if list_topping in available_toppings:
        print(f"Adding {list_topping}")
    else:
        print(f"Sorry, we don't have {list_topping}.")
print("Finished making your pizza!")

# Dictionary
alien_0 = {'color': 'green', 'points': 10}
print(alien_0['color'])
print(alien_0['points'])

# adding new key-value pairs
alien_1 = {'color': 'green', 'points': 10}
print(alien_1)
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)

alien_2 = {'color': 'green', 'points': 30}
new_points = alien_2['points']
print(f"you just earned {new_points} points")

# starting with an empty dictionary
alien_3 = {}
alien_3['color'] = 'green'
alien_3['points'] = 20
print(alien_3)

# modifying a dictionary
alien_4 = {'color': 'yellow'}
print(f"the alien is {alien_4['color']}.")
alien_4['color'] = 'green'
print(f"the alien color is now {alien_4['color']}")

alien_5 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# print(f"original position: {alien_5['x_position']}")
# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_5['speed'] == 'slow':
    x_increment = 1
elif alien_5['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
# the new position is the old position plus the increment
new_alien = alien_5['x_position'] + x_increment
print(f"new position: {new_alien}")

# deleting a value dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"Sarah favorite languages is {favorite_languages['sarah'].title()}.")

# Using get() to access values
# if the key you ask for does not exist, use get() method
alien_6 = {'color': 'green', 'speed': 'slow'}
print(alien_6.get('point', 'No point value assigned'))

# looping through a dictionary
user_0 = {
    'firstname': 'maysa',
    'lastname': 'fajirin',
    'username': 'may',
}
for key, value in user_0.items():
    print("\n" + key + ":")
    print(value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {languages}.")
for name in favorite_languages.keys():
    print(name)

favorite_languages1 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for key, value in favorite_languages1.items():
    print(f"Hi {key.title()}.")
    friends = ['phil', 'sarah']
    if key in friends:
        print(f"\t{key}, I see you love {value}!")

# You can also use the keys() method to find out if a particular key is not on the dictionary
alien_6 = {
    'color': 'green',
    'speed': 'slow'
}
if 'Erin' not in alien_6.keys():
    print("\n\tErin, please take our poll!")
# Looping Through a Dictionary’s Keys in a Particular Order
languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in sorted(languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
if 'Erin' not in sorted(alien_6.keys()):
    print("Erin, please take our poll!")

languages = {'python', 'ruby', 'python', 'c'}
for language in set(languages):
    print(language.title())

# Nesting
# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# A List in a Dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra Cheese']
}
print(f"you ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")

# A Dictionary in a Dictionary
users = {
    'Weinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'curie': {
        'first': 'marie',
        'last': 'muir',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print(f"\nusername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# sets
set1 = {"pop", "choke", "pop"}
print(set1)
album_list = ["michael jackson", "thriller", "thriller", 1982]
album_set = set(album_list)
print(album_set)

A = {"Thriller", "back in back", "msvc", "AC/DC"}
A.add("msvc")
print(A)
A = {"Thriller", "back in back", "msvc", "AC/DC"}
A.remove("back in back")

# using the while loop (infinite loops)
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nEnter 'quit' to end the program "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# guessing game using while
secret_word = "giraffe"
guess = ""
while guess != secret_word:
    guess = input("Enter guess: ")
print("you have won")

# guessing game using while
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_limit = False
while guess != secret_word and not out_of_limit:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_limit = True
if out_of_limit:
    print("you lose!")
else:
    print("you have won")

# using break
cities = "\nPlease enter the name of a city you would like to visit: "
while True:
    city = input(cities)
    if city == 'port harcourt':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(f"\t{current_number}")
