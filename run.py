import random

def new_deck():

    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = []
# Loops through suits and ranks to create cards and adds them to deck
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)

    random.shuffle(deck)

    return deck

# Takes card from shuffled deck and deals to player
def deal_Card(deck,player):
    card = deck.pop()
    player.append(card)
    return card

# Adds up total value of hand using dictionary and returns total
def hand_value(hand):

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

    total = 0

    for card in hand:
        total += values[card[0]] 
    
    if total <= 11 and 'A' in card:
        total += 10

    return total           



def main():
    player_go = True
    dealer_go = False
    deck = new_deck()
    player = []
    dealer = []

    for i in range(2):
        deal_Card(deck, player)
        deal_Card(deck, dealer)

    print(f"Your cards are {' '.join(player)}  Total: {(hand_value(player))}") 
    print(f"Dealers cards are {dealer[0]}, x") 
    
    while player_go == True:
        hit_or_stand = input("Would you like to [H]it or [S]tand: ")
        if hit_or_stand[0] == "H":
            deal_Card(deck, player)
            print(f"Your cards are {' '.join(player)} Total: {(hand_value(player))}")
        elif hit_or_stand[0] == "S":
            print(f"Dealer shows {' '.join(dealer)} Total: {(hand_value(dealer))}") 
            player_go = False
            dealer_go = True
            break
        else:
            print("Invalid input please press H to hit or S to stand") 
            
    
    
    while hand_value(dealer) < 17:
        deal_Card(deck, dealer)
        print(f"The dealer has {' '.join(dealer)} Total: {(hand_value(dealer))}")
        if hand_value(dealer) > 21:
            print(f"The dealer has {' '.join(dealer)} Total: {(hand_value(dealer))}")
            break


         

    



# Unit Test Section

main()






