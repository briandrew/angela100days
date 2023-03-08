############### Blackjack Project #####################

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 is the Ace.

#TODO: Create a deal_card() function that uses the List to *return* a random card

def deal_cards(card_list):
    for i in range(2):
        card_list.append(random.choice(cards))
   
#TODO 5: Deal the user and computer 2 cards each using deal_card() and append().

player_cards = []
dealer_cards = []

deal_cards(player_cards)
deal_cards(dealer_cards)

print(f"Initial player cards are {player_cards} and dealer cards are {dealer_cards}")

def calculate_score(card_list):
    total = sum(card_list)
    if total == 21:
        return 0
    if total >= 22:
        card_list.remove(11) 
        card_list.append(1) 
        total = sum(card_list)
    return total

player_score = calculate_score(player_cards)
print(f"player score is: {player_score}")

dealer_score = calculate_score(dealer_cards)
print(f"dealer score is: {dealer_score}")

game_going = True

if dealer_score == 0 and player_score == 0:
    print("You both have blackjack!")
elif dealer_score == 0:
    print("Dealer has blackjack!")
    print(f"And player has {player_score}")
    game_going = False
elif player_score == 0:
    print("Player has blackjack!")
    print(f"And dealer has {dealer_score}")
    game_going = False


def hit_me(card_list):
    card_list.append(random.choice(cards))
    return sum(card_list)
    


while game_going:
    hit = input("Want you another card? 'yes' or 'no'")
    if hit == 'yes':
        player_score = hit_me(player_cards)
        print(f"Your new  score is: {player_score}")
            
    elif hit == 'no':
        print(f'ok, you stay pat at {player_score}')

        
    if dealer_score > 21:
        print(f"Dealer is bust with a score of {dealer_score}")
    elif player_score > 21:
        print(f"Player busted out with a score of {player_score}")
    