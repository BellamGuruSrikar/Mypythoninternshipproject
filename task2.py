import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 5

print("Welcome to the Guessing Game!")
print(f"Try to guess the secret number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

else:
    print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}. Game over!")
