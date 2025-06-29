import random

# Constants
LOWER_BOUND = 1
UPPER_BOUND = 100

def evaluate_guess(guess, secret_number):
    """
    Compare user's guess with the secret number.
    Returns:
        'low' if guess < secret_number,
        'high' if guess > secret_number,
        'correct' if guess == secret_number
    """
    if guess < secret_number:
        return 'low'
    elif guess > secret_number:
        return 'high'
    else:
        return 'correct'

def play_guessing_game():
    """
    Starts an interactive number guessing game where the user
    tries to guess a randomly selected number between LOWER_BOUND and UPPER_BOUND.
    """
    print("\n🎯 Welcome to the Number Guessing Game!")
    print(f"I have selected a number between {LOWER_BOUND} and {UPPER_BOUND}.")
    print("Your task is to guess it correctly. Let's begin!\n")
    
    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    # print(secret_number)  # Uncomment for debugging
    attempts = 0

    while True:
        try:
            user_input = input(f"🔢 Enter your guess ({LOWER_BOUND}-{UPPER_BOUND}): ")
            guess = int(user_input)
            attempts += 1

            if guess < LOWER_BOUND or guess > UPPER_BOUND:
                print(f"⚠️ Please enter a number within the range of {LOWER_BOUND} to {UPPER_BOUND}.\n")
                continue

            result = evaluate_guess(guess, secret_number)

            if result == 'correct':
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
                print("✅ Thanks for playing!\n")
                break
            elif result == 'low':
                print("📉 Your guess is too low. Try a higher number.\n")
            elif result == 'high':
                print("📈 Your guess is too high. Try a lower number.\n")

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.\n")

# Run the game only when this file is executed directly
if __name__ == "__main__":
    play_guessing_game()
