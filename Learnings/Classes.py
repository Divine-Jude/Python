# Creating a Dog class
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


# making an instance
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


# Creating a Student Class
class student:
    """A simple attempt to model a student."""

    def __init__(self, Name, Major, Gpa, is_on_probation):
        self.Name = Name
        self.Major = Major
        self.Gpa = Gpa
        self.is_on_probation = is_on_probation

    # class function
    """Creating an object"""

    def on_honor_roll(self):
        if self.Gpa >= 3.5:
            return True
        else:
            return False


student1 = student("\nJim", "Business", 3.1, False)
student2 = student("Pam", "Art", 2.5, True)

print(student1.Name)
print(student2.on_honor_roll())


# Quiz test
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "\nWhat color are Bananas?\n(a) Magenta\n(b) Teal\n(c) Yellow\n\n",
    "\nWhat color are apples?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]


class Question:
    """A simple attempt to model a quiz"""

    def __init__(self, prompt, answer):
        """Initialize prompt and answer attributes"""
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]


def run_test(Questions):
    """Creating a list of Object Questions """
    score = 0
    for question in Questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)


# Inheritance
class Chef:

    def make_chicken(self):
        print("The chef makes a chicken.")

    def make_salad(self):
        print("The chef makes a salad.")

    def make_special_dish(self):
        print("The chef makes a bbq ribs.")


class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes a Orange Chicken.")

    def make_fried_rice(self):
        print("The chef makes fried rice")


myChef = Chef()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()

