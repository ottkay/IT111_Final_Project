#import random library to enable random choice selection for the computer
import random

#function to create user choices rock, paper or scissors with input validation
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in choices:
            return user_input
        print("Invalid choice. Please choose rock, paper, or scissors.")

#function to randomly generate the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

#function to determine winner
def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (
        (player1 == 'rock' and player2 == 'scissors') or
        (player1 == 'scissors' and player2 == 'paper') or
        (player1 == 'paper' and player2 == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"
#function that runs the game loops and displays results
def play_game():
    print("🪨 Welcome to Rock, Paper, Scissors! ✂️")

    #Game loop
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        #show both choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        #display the result
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}\n")

        #ask if the user wants to play another round
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break

#only run the game if this script is executed directly
if __name__ == "__main__":
    play_game()