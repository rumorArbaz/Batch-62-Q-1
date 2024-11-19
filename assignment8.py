import random

def for_numbers():
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    return player_number, computer_number

def user_guess(player_number):
    guess = ""
    while guess not in ["higher", "lower"]:
        guess = input(f"""Player number is {player_number}.
                      \nComputer number is higher or lower than the player number?: """).lower().strip()
    return guess  

def check_guess(player_number, computer_number, guess):
    if player_number == computer_number:
        print(f"The numbers are the same! It's a tie. The computer's number was {computer_number}.")
        return 0
    elif (guess == "higher" and computer_number > player_number) or (guess == "lower" and computer_number < player_number):
        print(f"You were right! The computer's number was {computer_number}.")
        return 1
    else:
        print(f"Wrong! The computer's number was {computer_number}.")
        return 0

def play_game():
    NUM_ROUNDS = 5
    score = 0

    print("\nWelcome to the High-Low Game!")
    print("--------------------------------")
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        
        player_number, computer_number = for_numbers()
        
        guess = user_guess(player_number)  # Fix: Now returns a valid guess
        
        score += check_guess(player_number, computer_number, guess)
        
        print(f"Your score is now {score}\n")

    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Perfect score! Great job!")
    elif score >= NUM_ROUNDS / 2:
        print("Nice job! You did well.")
    else:
        print("Better luck next time!")

play_game()