import random

# Define a list of quiz questions in the format (question, answer, choices)
quiz_questions = [
    ("What is the capital of France?", "Paris", ["London", "Berlin", "Paris", "Madrid"]),
    ("What is 7 x 8?", "56", ["42", "64", "56", "72"]),
    ("Which planet is known as the Red Planet?", "Mars", ["Venus", "Mars", "Jupiter", "Saturn"]),
    ("What is the largest mammal in the world?", "Blue whale", ["Dolphin", "Shark", "Blue whale", "Elephant"]),
]

# Function to present a quiz question and get the user's answer
def ask_question(question, answer, choices):
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    
    user_answer = input("Your answer (enter the number): ")
    return choices[int(user_answer) - 1]

# Function to play the quiz game
def play_quiz():
    score = 0
    
    # Shuffle the questions to make it more engaging
    random.shuffle(quiz_questions)
    
    for question, answer, choices in quiz_questions:
        user_choice = ask_question(question, answer, choices)
        
        if user_choice == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
    
    return score

# Function to display the final results
def display_results(score, total_questions):
    percentage = (score / total_questions) * 100
    print(f"You answered {score} out of {total_questions} questions correctly.")
    print(f"Your score: {percentage}%")
    
    if percentage >= 70:
        print("Congratulations! You did a great job!")
    else:
        print("You can do better. Keep learning!")

# Main program
if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    print("You will be presented with a series of multiple-choice questions.")
    print("Please select the correct answer by entering the corresponding number.")
    
    total_questions = len(quiz_questions)
    user_score = play_quiz()
    
    display_results(user_score, total_questions)
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        print("\nLet's play again!")
        user_score = play_quiz()
        display_results(user_score, total_questions)
    else:
        print("Thank you for playing!")

