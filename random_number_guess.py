import random
import inflect

p = inflect.engine()
secret_number = random.randint(1,100)
print(secret_number)

user_input = int(input("Guess a number between 1 and 100\n"))


tries = 0
while True:
    if type(user_input) == int:
        if user_input == secret_number:
            print("You guessed the correct number")
            break
        if user_input > secret_number:
            tries += 1
            print("You guessed too high, this is your", p.ordinal(tries), "try.")
            user_input = (input("Guess again.\n"))
        if (user_input) < secret_number:
            tries += 1
            print("You guessed too low, this is your", p.ordinal(tries), "try.")
            user_input = (input("Guess again.\n"))
    else:
        user_input = (input("Please enter a valid integer between 1-100\n"))


