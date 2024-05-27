import random

choices = ["scissor", "paper", "rock"]


def get_computer_choice():
    return random.choice(choices)


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'scissor' and computer_choice == 'paper') or \
            (user_choice == 'rock' and computer_choice == 'scissor') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"


def display_result(winner, user_score, computer_score):
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    if winner == 'tie':
        print("It's a tie")
    elif winner == 'user':
        print("You Won")
    else:
        print("You Lose")


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter one of the choices: scissor, rock, or paper: ").lower()

        while user_choice not in choices:
            user_choice = input("Enter a valid choice like scissor, rock, or paper: ").lower()

        computer_choice = get_computer_choice()

        winner = get_winner(user_choice, computer_choice)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        display_result(winner, user_score, computer_score)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
