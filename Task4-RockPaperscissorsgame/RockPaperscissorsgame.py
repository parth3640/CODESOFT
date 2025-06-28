import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\nRound {round_number}")
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        result = determine_winner(user, computer)

        if result == "tie":
            print("It's a tie.")
        elif result == "user":
            print("You win this round.")
            user_score += 1
        else:
            print("Computer wins this round.")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break
        round_number += 1

    print("\nGame Over.")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    play_game()