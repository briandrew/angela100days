#TODO generate random account from data file
from game_data import data
from random import randint

def get_random_celebrity():
    random_number = randint(0, len(data)-1)
    celebrity = data[random_number]
    return celebrity

user_correct = 0  #TODO keep score
game_on = True   

# loads initial contestants
a = get_random_celebrity()
b = get_random_celebrity()

while game_on:  #TODO make game repeatable
    #TODO format the account data in printable format
    print(f"A: {a['name']} is a {a['description']} from {a['country']}")

    print(f"B: {b['name']} is a {b['description']} from {b['country']}")

    #TODO get follower count for each account
    a_followers = a['follower_count']
    b_followers = b['follower_count']

    winner =''
    if a_followers > b_followers:
        winner = 'a'
    elif b_followers > a_followers:
        winner = 'b'

    print(winner)
    #TODO ask for a guess
    user_choice = input("Who has most followers, A or B? ").lower()
    #TODO use if statement to check if user is correct
    if user_choice == 'b' and winner == 'b':
        user_correct += 1
        print(f"You're right! Current score: {user_correct}")  #TODO give user feedback on guess
        print(f" {a['name']} has {a['follower_count']} followers")
        print(f" {b['name']} has {b['follower_count']} followers")
        a = b  #TODO making account at position 'b' become next account at 'a'
        b = get_random_celebrity()
    elif user_choice == 'a' and winner == 'a':
        user_correct += 1
        print(f"You're right! Current score: {user_correct}")  #TODO give user feedback on  guess
        print(f" {a['name']} has {a['follower_count']} followers")
        print(f" {b['name']} has {b['follower_count']} followers")
        a = b  #TODO making account at position 'b' become next account at 'a'
        b = get_random_celebrity()

    else:
        print("Sorry, you are wrong.")  #TODO give user feedback on their guess
        print(f"{a['name']} has {a['follower_count']} followers")
        print(f"{b['name']} has {b['follower_count']} followers")
        game_on = False    

print(f"You got {user_correct} correct!")

