import json
import os
print("Current working directory:", os.getcwd())

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to quiz_data.json
file_path = os.path.join(current_dir, 'quiz_data.json') 

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def load_quiz_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    quiz_data = data['quiz']
    return [Question(q['question'], q['options'], q['answer']) for q in quiz_data]

def welcome_message():
    print("Welcome to the Python Quiz!\n")

def display_question(question):
    print(question.prompt)
    for i, option in enumerate(question.options, start = 1):
        print(f"{i}. {option}")
    print()

def get_user_answer(options_count):
    while True:
        try:
            choice = int(input(f"Enter the number of your answer (1-{options_count}): "))
            if 1 <= choice <= options_count:
                return choice
            else:
                print(f"Please enter a number between 1 and {options_count}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions, start=1):
        print(f"Question {i}/{total_questions}:")
        display_question(question)

        user_choice = get_user_answer(len(question.options))

        if question.options[user_choice - 1] == question.answer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {question.answer}\n")

    return score

def thank_you_message(score, total_questions):
    print(f"Quiz completed! You scored {score} out of {total_questions}.")

def main():
    welcome_message()
    quiz_data = load_quiz_data(file_path)
    score = run_quiz(quiz_data)
    thank_you_message(score, len(quiz_data))

if __name__ == "__main__":
    main()