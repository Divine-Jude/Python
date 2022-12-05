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




