import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a random Number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry guess too low")
        elif guess > random_number:
            print("Sorry guess too high")
    
    print(f"Congrats you have gussed the Number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    Feedback = ""
    while Feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low    
        Feedback = input (f"is {guess} to high (H), too low (L) or is it correct (C)??"). lower()
        if Feedback == "h":
            high = guess - 1
        elif Feedback == "l":
           low = guess + 1

    print(f"Congrats the computer guessed your number, {guess} , correctly")       

computer_guess(1000)

