import random
import sys

options = ['r', 'p', 's']

user_score = 0
user_choices = []
computer_score = 0

def check_winner(user_selection):

    computer_selection = random.choice(options)
    print(f"Computer chose {computer_selection}")

    if user_selection == computer_selection:
        return "Tie"

    elif user_selection == 'p' and computer_selection == 'r':
        return "User"

    elif user_selection == 'p' and computer_selection == 's':
        return "Computer"

    elif user_selection == 'r' and computer_selection == 'p':
        return "Computer"
        
    elif user_selection == 'r' and computer_selection == 's':
        return "User"

    elif user_selection == 's' and computer_selection == 'r':
        return "Computer"

    elif user_selection == 's' and computer_selection == 'p':
        return "User"

    else:
        print("No winners....")
    
    return [computer_score, user_score]


def game():
    user_score = 0
    computer_score = 0
    while True:
        user_selection = input("Chose Rock[R], Paper[P], Scissors[S] or Quit[Q]").lower()
        if user_selection == 'q':
            sys.exit()
        if user_selection in options:
            user_choices.append(user_selection)
            print(f"User chose {user_selection}")
            winner = check_winner(user_selection)
            if winner == "User":
                user_score += 1
                print("You win!")
            elif winner == "Computer":
                computer_score +=1
                print("Computer wins!")
            else:
                print("Its a Tie!")
            print(f"User score: {user_score}" + "     |     " + f"Computer score: {computer_score}")
            print(user_choices)
            print("")
        else:
            print('Thats not a selection, try again..')


game()