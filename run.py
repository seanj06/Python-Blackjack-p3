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

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10':10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

    total = 0

    for card in hand:
        total += values[card[0]] 
    
    if total <= 11 and 'A' in card:
        total += 10

    return total           

hand = ['2x', '7x']
player_hand_value = hand_value(hand)
dealer_hand_value = hand_value(hand)
print(player_hand_value)
print(dealer_hand_value)

def main():
    deck = new_deck()
    player = []
    dealer = []



# Unit Test Section







