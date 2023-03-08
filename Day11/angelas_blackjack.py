############### Blackjack Project #####################
''' 
started with  my code from 'blackjack.py' and then changed per Angela's solution
'''

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 is the Ace.

def deal_cards():
    return random.choice(cards)
   
def calculate_score(cards):
    ''' Take a list of cards and return the sum of the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) 
        cards.append(1) 
    return sum(cards)

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return 'draw'
    elif dealer_score == 0:
        return 'you lose, dealer has blackjack'
    elif player_score == 0:
        return 'you win with blackjack'
    elif player_score > 21:
        return 'you busted'
    elif dealer_score > 21:
        return 'dealer busted, you win'
    elif player_score > dealer_score:
        return 'you win'
    else:
        return 'you lose'

def play_game():
    player_cards = []
    dealer_cards = []

    game_going = True

    for _ in range(2):
        player_cards.append(deal_cards()) 
        dealer_cards.append(deal_cards())

    while game_going:

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards are {player_cards} and dealer's showing card is {dealer_cards[0]}")
        print(f"player score is: {player_score} and dealer score is: {dealer_score}")
        if dealer_score == 0 or player_score == 0 or player_score > 21:
            game_going = False
        else:
            hit_me = input("Type 'y' to get another card, 'n' to stay pat: ")
            if hit_me == 'y':
                player_cards.append(deal_cards())
            else:
                game_going = False

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_cards())
        dealer_score = calculate_score(dealer_cards)

    print(compare(player_score, dealer_score))

while input("Up for a round of BlackJack? 'y' or 'n': ") == 'y':
    play_game()
    
