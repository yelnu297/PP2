import random

def guess_the_number():
    number = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    count = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        count += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break

guess_the_number()
