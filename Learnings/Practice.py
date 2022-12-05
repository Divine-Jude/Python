# # friend message
# character_name = "Eric"
# print("Hello " + character_name + ", " "would you like to learn some python today?")
#
# # name cases
# character_name = "Eric"
# print(character_name.lower())
# print(character_name.upper())
# print(character_name.title())
#
# # famous cases
# first_name = "Albert"
# last_name = "Einstein"
# famous_girlfriend = f"{first_name} {last_name}"
# message = " once said,“A girlfriend who never made a mistake never tried anything new.”"
# print(famous_girlfriend + message)
#
# # stripping name
# famous_fruit = '\tdivine\n'
# print("of all fruits", famous_fruit.rstrip(), "is my favorite")
#
# # getting input from users
#
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello, " + name + "! you are " + age)
#
# # List
# name = ['mimi', 'divine', 'emma', 'May']
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
#
# message = f"Hello {name[0].title()}, Hello {name[1].title()}, Hello {name[2].title()}, Hello {name[3].lower()}"
# print(message)
#
# transportation = ['car', 'Jet', 'Aeroplane', ]
# print("I will own a " + transportation[0].upper() + " at 28 ")
# print("I will ride a " + transportation[1] + " at 28 ")
# print("I will FLY ON! an " + transportation[2].upper() + " at 28 ")
#
# guest_list = ['divine', 'noble', 'stefan']
# message = f"Hello, {guest_list[0]} you are invited, Hello, {guest_list[1]} you are invited, Hello, {guest_list[2]}" \
#           f"you are invited "
# print(f"{guest_list[1]} said he can't make it")
#
# guest_list[1] = 'miracle'
# messages = "Hello, " + guest_list[0] + " you are invited," " Hello, " + guest_list[1] + "you are invited," "Hello, " \
#            + guest_list[2] + " you are invited"
# print(messages)
# print("Hello, guys i found a bigger table at this wedding ceremony, i will like to invite more people")
# guest_list.insert(0, 'Emmanuel')
# guest_list.insert(2, 'maysa')
# guest_list.append('mable')
# print( f"Hello, {guest_list[0]} you are invited, Hello, {guest_list[1]} you are invited, Hello, {guest_list[2]}" f"you are invited, Hello, {guest_list[3]} you are invited, Hello, {guest_list[4]} you are invited, Hello," f"{guest_list[5]} you are invited")
#
# locations = ['usa', 'italy', 'canada', 'germany', 'france']
# print(locations)
# print(sorted(locations))
# print(locations)
# print(sorted(locations, reverse=True))
# print(locations)
# locations.reverse()
# print(locations)
# locations.reverse()
# print(locations)
# locations.sort()
# print(locations)
# locations.sort(reverse=True)
# print(locations)
# print(len(locations))
#
# # loop
# pizzas = ['chicken', 'pepper', 'pepperoni']
# for pizza in pizzas:
#     print(pizza)
#     print(f"I like, {pizza.title()} pizza\n")
# print("I really Love pizza!\n")
#
# animals = ['dogs', 'cats', 'rabbit']
# for animal in animals:
#     print(animal)
#     print(f"A {animal.title()} would make a great pet\n")
# print("Any of these animals would make a great pet!")
#
# for value in range(1, 21):
#     print(value)
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 580, 5800, 5000, 23333]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
# odd_numbers = list(range(1, 20, 2))
# print(odd_numbers)
#
# multiples = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# for multiple in multiples:
#     print(multiple)
#
# cubes = []
# for value in range(1, 10):
#     cubes.append(value ** 3)
#     print(cubes)
#
# # list comprehension
# numbers = [value ** 3 for value in range(1, 10)]
# print(numbers)
#
# # slice
# my_foods = ['pizza', 'favail', 'carrot cake', 'cake', 'meat']
# print(f"The first three items in the list are: {my_foods[0:3]}")
# print(f"Three items from the middle of the list are: {my_foods[1:4]}")
# print(f"last three items in the list are: {my_foods[2:5]}")
#
# original_list = ['pizza', 'favail', 'carrot cake']
# friend_pizza = original_list[:]
# original_list.append('cake')
# friend_pizza.append('fish')
# print(original_list)
# print(f"noble favourite foods are {friend_pizza}")
# for pizza in original_list:
#     print(f"my favourite pizzas are: {pizza}")
# for pizza in friend_pizza:
#     print(f"\nmy favourite pizzas are: {pizza}")
# for my_food in my_foods:
#     print(my_food)
#
# # TUPLES
# foods = ('rice', 'beans', 'garri', 'yam', 'soup')
# for food in foods:
#     print(food)
# foods = ('cake', 'pizzas', 'chicken')
# print("\nmodified foods:")
# for food in foods:
#     print(food)
#
# # if statement
# car = 'subaru'
# car1 = 'audi'
# print(car == 'subaru')
# print(car1 == 'audi')
#
# food = 'Cake'
# if food.lower() == 'rice':
#     print(True)
# else:
#     print(False)
# number = 23
# if number >= 24:
#     print(True)
# else:
#     print(False)
#
# number0 = 24
# number1 = 18
# if number0 >= 22 and number1 >= 22:
#     print(True)
# else:
#     print(False)
#
# age0 = 22
# age1 = 18
# if age0 > 21 or age1 > 21:
#     print(True)
# else:
#     print(False)
#
# users = ['blessing', 'mimi', 'divine']
# user = 'maysa'
# if user not in users:
#     print(f"{user.title()}, you can post a response you wish")
# else:
#     print("his not the list")
#
# alien_color = ['green', 'yellow', 'red']
# if 'green' not in alien_color:
#     print("you have earned a 5 point")
# elif 'yellow' in alien_color:
#     print("you have earned 10 point")
# elif 'red' in alien_color:
#     print("you have earned 15 point")
# else:
#     print("you have earned 20 point")
#
# age1 = 20
# if age1 < 2:
#     print("you are a baby")
# elif age1 < 4:
#     print("you are a toddler")
# elif age1 < 13:
#     print("you are a kid")
# elif age1 <= 20:
#     print("you are a teenager")
# elif age1 < 65:
#     print("you are an adult")
# elif age1 >= 65:
#     print("you are an elder")
# else:
#     print("you are too little")
#
# favourite_fruits = ['apple', 'orange', 'pawpaw']
# if 'apple' in favourite_fruits:
#     print("you really like banana")
# if 'orange' in favourite_fruits:
#     print("you really like banana")
# if 'pawpaw' in favourite_fruits:
#     print("you really like banana")
# if 'bear' in favourite_fruits:
#     print("you really like banana")
# if 'mango' in favourite_fruits:
#     print("you really like banana")
#
# # printing for special characters
# usernames = ['div', 'admin', 'jaden']
# for username in usernames:
#     if username == 'admin':
#         print("hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {username}, thank you for logging in again.")
#
# # testing for empty list
# new_users = []
# if new_users:
#     for new_user in new_users:
#         print(f'hello {new_user}, thank you for logging in again.')
# else:
#     print("we need more users")
#
# current_users = ['div', 'admin', 'ron', 'john', 'mike']
# latest_users = ['ike', 'stefan', 'may', 'john', 'mike']
# for latest_user in latest_users:
#     if latest_user in current_users:
#         print("sorry you will need to enter a new username")
#     else:
#         print("username is available.")
#
# ordinal_numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# for ordinal_number in ordinal_numbers:
#     if ordinal_number == 1:
#         print(f"{ordinal_number}st")
#     elif ordinal_number == 2:
#         print(f"{ordinal_number}nd")
#     elif ordinal_number == 3:
#         print(f"{ordinal_number}rd")
#     elif ordinal_number == 4:
#         print(f"{ordinal_number}th")
#     elif ordinal_number == 5:
#         print(f"{ordinal_number}th")
#     elif ordinal_number == 6:
#         print(f"{ordinal_number}th")
#     elif ordinal_number == 7:
#         print(f"{ordinal_number}th")
#     elif ordinal_number == 8:
#         print(f"{ordinal_number}th")
#     elif ordinal_number == 9:
#         print(f"{ordinal_number}th")
#
# # dictionary
# girlfriend = {
#     'first name': 'maysa',
#     'last name': 'fajirin',
#     'age': '21',
#     'city': 'puwarkata'
# }
# print(girlfriend['first name'].title())
# print(girlfriend['last name'].title())
# print(girlfriend['age'])
# print(girlfriend['city'].title())
#
# favourite_numbers = {'Divine': 24, 'Jude': 8, 'Mike': 6, 'May': 12}
# print(favourite_numbers['Divine'])
# print(favourite_numbers['Jude'])
# print(favourite_numbers['Mike'])
# print(favourite_numbers['May'])
#
# # using loop in dictionary
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# names = ['jen', 'peter', 'ugo', 'edward', 'phil', 'sarah']
# for name in names:
#     if name in favorite_languages:
#         print(f"{name.title()}, thank you for taking the poll.")
#     else:
#         print(f"{name.title()}, please take our poll!")
#
# squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
# new_squares = []
# i = 0
# while i < len(squares) and squares[i] == 'orange':
#     new_squares.append(squares[i])
#     i = i + 1
# print(new_squares)
#
# PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# Rating = PlayListRatings[0]
# i = 0
# while i < len(PlayListRatings) and Rating >= 6:
#     print(Rating)
#     Rating = PlayListRatings[i]
#     i = i + 1
#
# # The break Statement
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i = i + 1
#
# # The continue Statement
# i = 0
# while i < 6:
#     i = i + 1
#     if i == 3:
#         continue
#     print(f"\t{i}")
#
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")
#
# # Using a while Loop with Lists and Dictionaries [Moving Items from One List to Another]
# sandwich_orders = ["tuna", "pizza", "chicken", "ice cream"]
# finished_sandwich = []
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     finished_sandwich.append(current_sandwich)
#     print(f"i have made your made your {current_sandwich} sandwich")
# print("\nThe following sandwich have been confirmed:")
# for finished_sandwich in finished_sandwich:
#     print(finished_sandwich)
#
#
# # Functions
# def say_hi(person, ages):
#     print("Hello " + person + ", you are " + ages)
#
#
# say_hi("Mike", "25")
# say_hi("steve", "27")
#
#
# # using function and return statement
# def cube(num):
#     return num * num * num
#
#
# print(cube(4))
#
# x = 'go'
# if x == 'go':
#     print(x)
# else:
#     print('stop')
#
# for i, x in enumerate(['a', 'b', 'c']):
#     print(i + 1, x)
#
#
# def greet_user(user_name):
#     """display a simple greeting."""
#     print(f"hello, {user_name}")
#
#
# greet_user('eve')
#
#
# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name}.")
#
#
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
#
#
# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name}.")
#
#
# # using keyword arguments
# describe_pet(animal_type='hamster', pet_name='harry')
#
#
# # using default values
# def describe_pet(pet_name='willie', animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
#
# describe_pet()
#
#
# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
#
# # Equivalent Function Calls
# describe_pet('willie')
#
#
# # describe_pet(pet_name='willie')
#
# # using return statement
# def get_formatted(F_name, L_name):
#     """return a full name, neatly formatted."""
#     full_name = f"{F_name} {L_name}"
#     return full_name.title()
#
#
# musician = get_formatted('jimi', 'hendrix')
# print(f"\n {musician}")
#
#
# # Making an Argument Optional
# def get_formatted_name(firstname, lastname, middle_name=''):
#     """return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{firstname} {lastname} {middle_name}"
#     else:
#         full_name = f"{firstname} {lastname}"
#     return full_name
#
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician.title())
#
# musician = get_formatted_name('john', 'hooker')
# print(musician.title())
#
#
# # returning a dictionary
# def build_person(firstname, lastname, N_age=None):
#     """Return a dictionary of information about a person."""
#     person = {'first': firstname, 'last': lastname}
#     if N_age:
#         person['date_of_birth'] = N_age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', '27')
# print(musician)
#
#
# # using a function with a while loop
# def get_formatted_name(f_names, ls_names):
#     """Return a full name, neatly formatted."""
#     full_name = f"{f_names} {ls_names}"
#     return full_name.title()
#
#
# # this is an infinite loop!
# while True:
#     print("\nplease tell me your name: ")
#     print("Enter 'quit' to stop at anytime")
#     f_name = input("\tfirst name: ")
#     if f_name == 'quit':
#         break
#
#     ls_name = input("\tlast name: ")
#     if ls_name == 'quit':
#         break
#
#     formatted = get_formatted_name(f_name, ls_name)
#     print(f"\n Hello, {formatted}!")
#
# name = input("Enter your name: ")
# age = input("Enter your name: ")
# print("Hello! " + name + " you are " + age)
# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")
# result = float(num1) + float(num2)
# print(result)
#
#
# # functions
# def say_hi(N_name, N_age):
#     print("Hello " + N_name + ", you are " + N_age)
#
#
# say_hi("Mike", "35")
# say_hi("Div", "70")
#
#
# # return statement
# def cube(num):
#     return num * num * num
#
#
# result = cube(4)
# print(result)
#
# # if statement
# is_male = False
# is_tall = True
# if is_male and is_tall:
#     print("you are a tall male")
# elif is_male and not is_tall:
#     print("you are a male but you are short")
# elif not is_male and is_tall:
#     print("you are not a male but are tall")
# else:
#     print("you are not male or not tall")
#
#
# # if statement and comparison
# def max_num(nums1, nums2, nums3):
#     if nums1 >= nums2 and nums1 >= nums3:
#         return num1
#     elif nums2 >= nums1 and nums2 >= nums3:
#         return nums2
#     else:
#         return nums3
#
#
# rental_cars = input("What kind of rental car do you want?: ")
# if rental_cars == "benz":
#     print(f'Let me see if I can find you a {rental_cars}')
# if rental_cars == "subaru":
#     print(f'Let me see if I can find you a {rental_cars}')
#
# Restaurant_Seating = input("how many people are in their dinner group?: ")
# Restaurant_Seating = int(Restaurant_Seating)
# if Restaurant_Seating >= 8:
#     print(f'you will have to wait for a table ')
# else:
#     print(f'the table is ready ')
#
# user = input("Enter a number: ")
# user = int(user)
# if user % 10 == 20:
#     print("user is a multiple 10")
# else:
#     print("user is not multiple of 10")
#
# # Storing Your Functions in Modules
# # Importing an Entire Module
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# # # Now we’ll make a separate file called making_pizzas.py in the same
# # # directory as pizza.py. This file imports the module we just created and then
# # # makes two calls to make_pizza():
# # # import Pizza
# #
# # Pizza.make_pizza(12, 'pepperoni')
# # Pizza.make_pizza(16, 'mushrooms', 'green peppers', "extra cheese")
#
#
# # # Using as to Give a Module an Alias
# # # import pizza as p
# #
# # p.make_pizza(16, 'pepperoni')
# # p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#
#
# # # Importing Specific Functions
# # # from pizza import make_pizza
# #
# # make_pizza(16, 'pepperoni')
# # make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#
#
# # # from pizza import make_pizza as mp
# #
# # mp(16, 'pepperoni')
# # mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#
#
# # 2D lists and Nested loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# print(number_grid[1][0])
#
# for row in number_grid:
#     print(row)
#
# for row in number_grid:
#     for col in row:
#         print(col)
#
# # try except
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Invalid Input")
#
#
# # Writing Files
# employee_file = open("Employees.csv", "w")
# employee_file.write("\nKelly - Customer service")
# employee_file.close()
#
# # Appending Files
# employee_file = open("Employees.csv", "a")
# employee_file.write("\nToby -  Human Resources")
# employee_file.close()
#
# # Reading Files
# employee_file = open("Employees.csv", "r")
# print(employee_file.read())
# employee_file.close()
#
#
# # Classes and Object
# class Restaurant:
#     """A simple attempt to model a restaurant"""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize attributes to describe a Restaurant"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"I love going to {self.restaurant_name} Restaurant.")
#
#     def open_restaurant(self):
#         print(f"Cuisine type is '{self.cuisine_type}', It is considered the world most refined and elegant style of "
#               "cooking.")
#
#
# restaurant = Restaurant("Genesis", "French Cuisine")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
#
# class Car:
#     """A simple attempt to represent a car"""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 24
#
#     def get_descriptive_name(self):
#         """Return a nearly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage"""
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("you can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
#
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
#
#
# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=75):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has {self.battery_size}-kwh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 75:
#             ranges = 260
#         elif self.battery_size == 100:
#             ranges = 315
#         print(f"This car can go about {ranges} miles on a full charge")
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()  # Instances as Attributes
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
#
#
# import Car
#
# my_beetle = Car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = Car.ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())
#
# from random import randint
# from random import choice
#
# print(randint(1, 6))
# players = ['charles', 'martina', 'florence', 'eli']
# first_up = choice(players)
# print(first_up)

with open('pi_digits.txt') as file_object:
    lines = file_object.read()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi")
