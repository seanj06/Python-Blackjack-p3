import random


def new_deck():
    """
    Creates a new deck of new cards using suit and ranks lists and shuffles
    """

    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
# Loops through suits and ranks to create cards and adds them to deck
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)

    random.shuffle(deck)

    return deck


def deal_card(deck, player):
    """
    Takes card from shuffled deck and deals to player
    """
    card = deck.pop()
    player.append(card)
    return card


def hand_value(hand):
    """
    Adds up total value of hand using dictionary and returns total
    """

    values = {'1': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    total = 0
    aces = 0
    card = ''
    for card in hand:
        total += values[card[0]] 
    if card[0] == 'A':
        aces += 1

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1 

    return total

            
def main():
    """
    Main game loop
    """
    player_go = True
    dealer_go = False
    deck = new_deck()
    player = []
    dealer = []

    for i in range(2):
        deal_card(deck, player)
        deal_card(deck, dealer)

    print(f"Your cards are {' '.join(player)}  Total: {(hand_value(player))}") 
    print(f"Dealers cards are {dealer[0]}, x") 
    while player_go is True and hand_value(player) < 21:
        hit_or_stand = input("Would you like to [H]it or [S]tand: ")
        if hit_or_stand[0] == "H":
            deal_card(deck, player)
            print(f"Your cards are {' '.join(player)} Total: {(hand_value(player))}")
        elif hit_or_stand[0] == "S":
            print(f"Dealer shows {' '.join(dealer)} Total: {(hand_value(dealer))}") 
            player_go = False
            dealer_go = True
            break
        else:
            print("Invalid input please press H to hit or S to stand") 
            
    
    
    while hand_value(dealer) < 17:
        deal_card(deck, dealer)
        print(f"The dealer has {' '.join(dealer)} Total: {(hand_value(dealer))}")
        if hand_value(dealer) > 21:
            print(f"The dealer has busted you win")

    if hand_value(dealer) > hand_value(player) and hand_value(dealer) < 22:
        print("Dealer wins")  
    elif hand_value(dealer) > hand_value(player) and hand_value(dealer) == 21:
        print("Dealer wins with a blackjack!")    
    elif hand_value(player) > hand_value(dealer) and hand_value(player) < 22:
        print("You win") 
    elif hand_value(player) > hand_value(dealer) and hand_value(player) == 21:
        print("You win with a blackjack!")    
    elif hand_value(player) == hand_value(dealer):
        print("Its a draw")  
    elif hand_value(player) > 21:
        print("Sorry you bust")
        
              



         

    



# Unit Test Section

main()





