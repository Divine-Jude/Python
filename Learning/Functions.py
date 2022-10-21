# Defining a Function
# Here’s a simple function named greet_user() that prints a greeting
def greet_user():
    """Display a simple greeting"""
    print("Hello!")


greet_user()


# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")


greet_user('Jesse')


# Passing Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('Hamster', 'Harry')
describe_pet("dog", "willie")


# Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')


# Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name="willie")
describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')


# Return Values
def get_formatted_name(first_name, last_name):
    """Return a fullname, neatly formatted"""
    full_name = f"\n{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print(get_formatted_name('jimi', 'hendrix'))


# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a fullname, neatly formatted"""
    if middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"
    else:
        full_name = f"\n{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'hooker')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# using a function with a while loop
# def get_formatted_name(first_name, last_name):
#     """Return a fullname, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     print("(Enter 'quit' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'quit':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'quit':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"Hello, {formatted_name.title()}!")


# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function

# Consider a company that creates 3D printed models of designs that users submit. Designs that need to be printed are
# stored in a list, and after being printed they’re moved to a separate list. The following code does this without
# using functions Start with some designs that need to be printed:

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# We can reorganize previous code by writing two functions
def print_models(unprinted_designs_1, completed_models_2):
    """
    simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs_1:
        current_designs = unprinted_designs_1.pop()
        print(f"\nPrinting Model: {current_designs}")
        completed_models_2.append(current_designs)


def show_completed_models(completed_models_2):
    """show all the models that were printed."""
    print("\nThe following models have been printed:")
    for complete_model in completed_models_2:
        print(complete_model)


unprinted_design_1 = ['phone case', 'robot pendant', 'dodecahedron']
completed_models_2 = []
print_models(unprinted_design_1[:], completed_models_2)
show_completed_models(completed_models_2)


# to keep the original list of unprinted designs for your records.
# unprinted_design_1(unprinted_design_1[:])

# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')


# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

# Styling functions
# If you specify a default value for a parameter, no spaces should be used on either side of the equal sign:

# def function_name(parameter_0, parameter_1='default value')

# The same convention should be used for keyword arguments in function calls:
# print function_name(value_0, parameter_1='value')
