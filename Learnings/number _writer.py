# # Storing Data and loading Data Using json.dump() and json.load()
# json.dump()
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# json.load()
filename = 'numbers.json'
with open(filename) as f:
    number = json.load(f)

print(number)

# Saving and reading user-generated Data
username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"\nWe'll remember you when you come back, {username}!")

# new program that greets a user whose name has already been stored:
Filename = 'username.json'

with open(Filename) as f:
    user = json.load(f)
    print(f"\nWelcome come back, {user}!")

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome come back, {username}!")


# Refactoring
def greet_user():
    """Greet the user by name."""
    file = 'username.json'

    try:
        with open(filename) as fn:
            users = json.load(fn)
    except FileNotFoundError:
        users = input("What is your name? ")
        with open(file, 'w') as fn:
            json.dump(users, fn)
            print(f"We'll remember you when you come back, {users}!")
    else:
        print(f"Welcome come back, {users}!")


greet_user()


# Let’s refactor greet_user() so it’s not doing so many tasks.
# We’ll start by moving the code for retrieving a stored username to a separate function:

def get_stored_username():
    """Get stored username if available."""
    file_name = 'username.json'
    try:
        with open(file_name) as file_object:
            Username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return Username


def get_new_username():
    """Prompt for a new username."""
    users_name = input("What is your name? ")
    filenames = 'username.json'
    with open(filenames, 'w') as fs:
        json.dump(users_name, fs)
    return users_name


def greet_users():
    """Greet the user by name."""
    user_name = get_stored_username()
    if user_name:
        print(f"Welcome come back, {user_name}!")
    else:
        usernames = input("What is your name? ")
        file_name = 'username.json'
        with open(file_name, 'w') as fn:
            json.dump(usernames, fn)
            print(f"We'll remember you when you come back, {usernames}!")


greet_users()
