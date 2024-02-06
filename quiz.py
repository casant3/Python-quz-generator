
question_1 = "What is the capital of France?"
options_1 = ["London", 
             "Rome",
             "Paris", 
             "Berlin"]
correct_answer_1 = "Paris"
    
question_2 = "What is the largest planet in our solar system?"
options_2 = ["Mars", 
             "Jupiter", 
             "Earth", 
             "Saturn"]
correct_answer_2 = "Jupiter"

question_3 = "Who wrote 'Romeo and Juliet'?"
options_3 = ["Charles Dickens", 
             "Jane Austen", 
             "Mark Twain",
             "William Shakespeare"]
correct_answer_3 = "William Shakespeare"

question_4 = "What is the chemical symbol for water?"
options_4 = ["H2O", 
             "CO2", 
             "O2", 
             "NaCl"]
correct_answer_4 = "H2O"
    
question_5 = "Which animal is known as the 'king of the jungle'?"
options_5 = ["Elephant", 
             "Tiger",
             "Lion", 
             "Giraffe"]
correct_answer_5 = "Lion"

questions = [
{"question": question_1, "options": options_1, "correct_answer": correct_answer_1},
{"question": question_2, "options": options_2, "correct_answer": correct_answer_2},
{"question": question_3, "options": options_3, "correct_answer": correct_answer_3},
{"question": question_4, "options": options_4, "correct_answer": correct_answer_4},
{"question": question_5, "options": options_5, "correct_answer": correct_answer_5}
]
    
    
import random
import colorama
from colorama import Fore
colorama.init()

while True:
    score = 0

    # Shuffle the questions
    random.shuffle(questions)

    for index in range(len(questions)):
        question_data = questions[index]
        #\n = new line
        print(f"\nQuestion {index + 1}: {question_data['question']}")
        for i in range(len(question_data['options'])):
            option = question_data['options'][i]
            print(f"{i + 1}. {option}")
        
        # User input
        answer = input("Your answer (1-4): ")
        
        # check if the answer is right
        #.isdigit() checks if the input provided by the user consists entirely of digits (0-9)
        # 1 <= int(answer) <= 4: converts the input string to an integer using int(answer) and then checks if the resulting integer falls within the range from 1 to 4 (inclusive)
        if answer.isdigit() and 1 <= int(answer) <= 4:
            selected_option = question_data['options'][int(answer) - 1]
            if selected_option == question_data['correct_answer']:
                print(Fore.GREEN + "Correct!")
                score += 5
            else:
                print(Fore.RED + f"Incorrect. The correct answer is: {question_data['correct_answer']}")
                score -= 2
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

        print(Fore.WHITE)

    # final score
    print(f"\nYour score: {score}/{len(questions) * 5}")

    # ask if the user wants to play again
    repeat = input("Do you want to play again? (yes/no): ")
    if repeat.lower() != "yes":
        break