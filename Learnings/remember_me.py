import json


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
    new_username = input("What is your name? ")
    filenames = 'username.json'
    with open(filenames, 'w') as fs:
        json.dump(new_username, fs)
    return new_username


def greet_users():
    """Greet the user by name."""
    user_name = get_stored_username()
    if user_name:
        print(f"Welcome come back, {user_name}!")
    else:
        new_user = get_new_username()
        print(f"We'll remember you when you come back, {new_user}!")


greet_users()
