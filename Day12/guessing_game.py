
#Number Guessing Game Objectives:


# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo =  '''
  ________                                                            ___.                 
 /  _____/ __ __   ____   ______ ______  _____      ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  \__  \    /    \|  |  \/     \| __ \_/ __ \_  __\\
\    \_\  \  |  /\  ___/ \___ \ \___ \    / __ \_ |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  (____  / |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/        \/       \/            \/    \/     \/       
'''
import random
# create these as example of global constants that shouldn't change
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)


def set_difficulty():
    level = input("Would you like it 'easy' or 'hard': ").lower()
    if level.strip() == 'easy':
        return EASY_LEVEL_TURNS
    elif level.strip() == 'hard':
        return HARD_LEVEL_TURNS

def check_answer(guess, actual_number, guesses):
    if guess == actual_number:
        print("You guessed it!")
        exit()
        
    elif guess > actual_number:
        print("Too high")
        return guesses -1
        
    elif guess < actual_number:
        print("Tool low")
        return guesses -1

def game():     
    actual_number = random.randint(1, 100)
    print("I'll pick a number between 1 - 100")
    print("Then you try and guess it")

    guesses = set_difficulty()

    print(f"You get {guesses} guesses.")

    while guesses > 0:
        guess = int(input("Guess a number between 1 - 100: "))
        guesses = check_answer(guess, actual_number, guesses)
        print(f"You have {guesses} guesses remaining")
        
    if guesses == 0:
        print(f"Rats, you ran out of guesses. The actual number was {actual_number}")

game()