import random
import time

def welcome_message():
    print("\n🎮 Welcome to the Advanced Number Guessing Game!")
    print("Guess the number I'm thinking of between 1 and 100.")
    print("Choose a difficulty level to begin...\n")

def choose_difficulty():
    print("Difficulty Levels:")
    print("1. Easy   (Unlimited attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard   (5 attempts)")

    while True:
        choice = input("Select difficulty (1/2/3): ")
        if choice == '1':
            return None  # Unlimited attempts
        elif choice == '2':
            return 10
        elif choice == '3':
            return 5
        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def play_game(max_attempts):
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    while max_attempts is None or attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempt(s) and {total_time} seconds.")
            return calculate_score(attempts, total_time, max_attempts)

        if max_attempts and attempts == max_attempts:
            print(f"\n💀 You've used all {max_attempts} attempts. The number was {secret_number}.")
            return 0

def calculate_score(attempts, total_time, max_attempts):
    base_score = 1000
    time_penalty = int(total_time * 5)
    attempt_penalty = attempts * 20
    difficulty_bonus = 100 if max_attempts == 5 else (50 if max_attempts == 10 else 0)

    score = base_score - time_penalty - attempt_penalty + difficulty_bonus
    return max(score, 0)

def main():
    welcome_message()
    max_attempts = choose_difficulty()
    score = play_game(max_attempts)
    print(f"\n🏆 Your final score: {score}\n")
    print("🔁 Play again to improve your score!")

if __name__ == "__main__":
    main()
