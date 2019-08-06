import random


class Quizmaster:

    def __init__(self, min_range, max_range):
        self.min_range = min_range
        self.max_range = max_range

        self.left_operand = 0
        self.right_operand = 0

        self.answer = 0;
        self.in_progress = False

    def get_plus_question(self):
        self.left_operand = random.randint(self.min_range, self.max_range)
        self.right_operand = random.randint(self.min_range, self.max_range)

        question = f"{self.left_operand} + {self.right_operand} = "
        return question


    def calculate_answer(self):
        self.answer = self.left_operand+self.right_operand
        return self.answer


    def reset(self):
        self.left_operand = 0
        self.right_operand = 0
        self.answer = 0;


    def start_quiz(self):
            print('\nLets play the math game and try some addition questions.....')
            self.min_range = int(input("\nEnter the min range: "))
            self.max_range = int(input("\nEnter the max range: "))
            self.ask_question()

    def will_play_again(self):
        user_choice = input("It is fun and a good practice for basic math, do you want to continue with it? ")
        if user_choice == 'y' or user_choice =='yes':
            self.ask_question()
        else:
            print("Thanks for playing with me, hope you liked it...")


    def ask_question(self):
        self.reset()
        user_answer = int(input(self.get_plus_question()))
        correct_answer = self.calculate_answer()
        if user_answer == correct_answer:
            print("Well Done, that was correct.\n")
        else:
           print("That was not correct, now try again...\n")
        self.ask_question()


quiz_master = Quizmaster(0, 20)
quiz_master.start_quiz()


