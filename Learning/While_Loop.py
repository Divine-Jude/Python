# While loops and user input
message = input("tell me something, and i will repeat it back to you: ")
print(message)

name = input("please enter your name: ")
print(f'\nHello, {name}!')

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f'\nHello, {name}!')

age = input("How old are you? ")
print(f"i am {age}")

# input
height = input("How tall are you, in inches? ")
heights = int(height)
if heights >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# input
# using modulo operator
number = input("enter a number, and i'll tell you if it's even or odd: ")
numbers = int(number)
if numbers % 2 == 0:
    print(f"\n the number {numbers} is even")
else:
    print(f"\n the number {numbers} is odd")

# Avoiding Infinite Loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number = current_number + 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# using flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I will Love to Visit {city}!")

# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(f"\n{current_number}")

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"Verifying user: {current_users}")
    confirmed_users.append(current_users)
print("\nFollowing users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a Dictionary with User Input
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    name = input("\nwhat is your name? ")  # Prompt for the person's name and response
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
    # Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
for pet in pets:
    print(f"\t{pet}")
