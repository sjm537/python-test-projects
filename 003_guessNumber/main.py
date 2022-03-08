import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")

playGuessNum = input("Would you like to play? Y or N\n")

while playGuessNum == "Y":
    
    n = int(input("Pick a maximum number for the computer to pick from: "))
    guess(n)
    
    playGuessNum = input("Would you like to play again? Y or N")

else:
    print ("Goodbye!")



 


