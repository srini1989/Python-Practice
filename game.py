import random

guesses_taken = 0
print("Hello! What is your name ?")
name = input()

number = random.randint(1, 20)
print("Well, {} I am thinking of a number between 1 and 20.".format(name))

while guesses_taken < 6:
    print("Take a guess.")
    guess = input()
    guess = int(guess)
    guesses_taken += 1

    if guess < number:
        print("your guess too Low...")
    if guess > number:
        print("Your guess is too High...")
    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print("Good Job, {}. You guessed my number in {} guesses !".format(name, guesses_taken))

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was {}".format(number))
