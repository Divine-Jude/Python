# # relative path
# with open('text_files/filename.txt') as file_object:

# # Absolute path
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# Reading from a file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# Reading Line by Line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
for line in lines:
    print(line.rstrip())

# Working with a File’s Contents
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# writing to a file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and
# write to the file ('r+').

# Writing Multiple Lines
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("\nI love creating new games.")

# Appending to a file
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.")
    file_object.write("\nI love creating apps that can run in a browser.")

# Exceptions
# Handling the ZeroDivisionError Exception
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# # Using Exceptions to Prevent Crashes
# print("\nGive me two numbers, and I'll divide them.")
# print("Enter 'q' to quit")
#
# while True:
#     first_number = input("\nFirst Number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second Number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# Handling the FileNotfoundError Exception
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# Analyzing Text
title = "Alice in Wonderland"
print(title.split())

filename = 'programming.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


# Working with Multiple Files
def count_words(file_names):
    """Count the approximate number of words in a file."""
    try:
        with open(file_names, encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_names} does not exist.")
    else:
        word = content.split()
        num_word = len(word)
        print(f"\nThe file {file_names} has about {num_word} words.")


file_name = 'alice.txt'
count_words(file_name)

filenames = ['programming.txt', 'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# Failing Silently
def count_words(file_nam):
    """Count the approximate number of words in a file."""
    try:
        with open(file_nam, encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        pass
    else:
        word = content.split()
        num_word = len(word)
        print(f"\nThe file {file_nam} has about {num_word} words.")


file_names = 'alice.txt'
count_words(file_names)

filenames = ['programming.txt', 'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

