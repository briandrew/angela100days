
from game_data import data
import random

def format_data(account):
    """ Takes account data and returns the printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """ Takes user's guess and follower accounts and returns whether user correct """
    if a_followers > b_followers:
        return guess == 'a'  # returns True or False depending on whether user guess = 'a'
    else:
        return guess == 'b'

score = 0
game_should_continue = True  #flag

b = random.choice(data)  # pre-populate 'b' so can set 'a' to 'b' below

while game_should_continue:
    #TODO generate random account from data file
    #TODO making account at position 'b' become next account at 'a'
    a = b  # which allows us to bump 'b' up to 'a' to continue the comparison
    b = random.choice(data)

    while a == b:  # avoid ties
        b = random.choice(data)

    print(f"Compare A: {format_data(a)}.")
    print('vs')
    print(f"Against B: {format_data(b)}")

    #TODO ask for a guess
    guess = input("Which has more followers? Type 'A' or 'B': ").lower()


    #TODO get follower count for each account
    a_follower_count = a['follower_count']
    b_follower_count = b['follower_count']
    #TODO check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #TODO give user feedback on their guess
    if is_correct:
        score += 1  #TODO keep score
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")


