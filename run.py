import random
import time
import sys
import pyfiglet


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


def type_text(text):
    """
    Gives printed messages typewriter effect
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


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

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              '1': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

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


def check_winner(dealer, player, chips):
    """
    Compares total hand values of dealer and player and determines winner
    """ 
    if hand_value(player) == 21 and hand_value(dealer) != 21:
        print("You win with a blackjack")
        player_chips.win_bet()
    elif hand_value(dealer) == 21 and hand_value(player) != 21:
        print("Dealer wins with a blackjack")
        player_chips.lose_bet()
    elif hand_value(player) > 21:
        print("Sorry you have busted") 
        player_chips.lose_bet()
    elif hand_value(dealer) > 21 and hand_value(player) < 22:
        print("Dealer busts you win") 
        player_chips.win_bet()       
    elif hand_value(player) == hand_value(dealer):
        print(f"You both have {hand_value(player)} its a draw") 
    elif 21 - hand_value(player) < 21 - hand_value(dealer):
        print("You win") 
        player_chips.win_bet()
    elif 21 - hand_value(dealer) < 21 - hand_value(player):
        print("Dealer wins")  
        player_chips.lose_bet()


def main():
    """
    Main game loop
    """
    playing = True
    while playing:       
        player_go = True
        deck = new_deck()
        player = []
        dealer = [] 
        print(f"You have {player_chips.chip_balance} chips ")
        bet(player_chips)
        for i in range(2):
            deal_card(deck, player)
            deal_card(deck, dealer)
        print(f"\nYour cards are {' '.join(player)} \
             Total: {(hand_value(player))}\n") 
        print(f"Dealers cards are {dealer[0]}, x\n") 
        while player_go is True and hand_value(player) < 21:
            try:
                hit_or_stand = input("Would you like to [H]it or [S]tand: ")
                if hit_or_stand.lower() == "h":
                    deal_card(deck, player)
                    print(f"Your cards are {' '.join(player)} \
                        Total: {(hand_value(player))}")
                elif hit_or_stand.lower() == "s":
                    print(f"Dealer shows {' '.join(dealer)} \
                        Total: {(hand_value(dealer))}") 
                    player_go = False
            except ValueError:
                print("Invalid input please press H to hit or S to stand")         
        while hand_value(dealer) < 17 and hand_value(player) < 22:
            deal_card(deck, dealer)
            print(f"The dealer has {' '.join(dealer)}\
                 Total: {(hand_value(dealer))}")

        check_winner(dealer, player, Chips) 
        print(f"You have {player_chips.chip_balance} chips")
        if player_chips.chip_balance == 0:
            print("Sorry you have run out of chips, game over!")
            playing = False
            player_chips.chip_balance = 500
        play_again()
        

def start_screen():
    """
    Start screen message user sees when game first runs
    """
    welcome_message = pyfiglet.figlet_format("Welcome To Blackjack")
    print(welcome_message)
    while True:
        try:
            start_game = input("Press [S] to start the game or press [I] to "
                               "read the instructions \n").strip()
            if start_game.lower() == 's':
                name_input()
            elif start_game.lower() == 'i':
                instructions()       
        except ValueError:
            print("Invalid input") 
        else:
            print("Invalid input")    
        

def play_again():
    """
    Prompts user at game end if they want to play again
    """
    while True:
        try:
            play_again = input("Would you like to play again? [Y] or [N]")
            if play_again.lower() == 'y':
                main()
            elif play_again.lower() == 'n':
                print(" Thanks for playing Goodbye")
                player_chips.chip_balance = 500
                start_screen()
        except ValueError:  
            print("Invalid input")
            continue  
        else:
            print("Invalid input please type Y for yes or N for no")


def name_input():
    """
    Function for user to enter their name on game start
    """
    while True:
        try:
            player_name = input("Please enter your name \n").strip()
            if player_name.isalpha():
                type_text(f"Welcome to the game {player_name} ")
                main()
        except ValueError:
            print("Invalid input") 
        else:
            print("Invalid input please enter your name")


def instructions():
    """
    Function to show player game instructions
    """ 
    type_text("Welcome to blackjack the card game of skill and luck.\n\n "
              "The aim of the game is to get to as close to 21 as you can "
              "without going over it.\n\n "
              "If you do you will bust!\n\n "
              "Each card number is worth that value, Jacks, Queens " 
              "and Kings\n "
              "are worth 10 and Aces are worth both 1 and 11.\n\n "
              "You will be dealt 2 cards at the start of the game and will be "
              "given a choice wether to hit or stand.\n\n "
              "If you choose hit you will be dealt another card and if you "
              "choose stand it is the dealers turn.\n\n "
              "The dealer will also be dealt 2 cards but you will only be "
              "shown 1 until you have completed your turn.\n\n "
              "The dealer has to take another card if they have "
              "less than 17.\n\n") 
    main_menu = input("Press any key to return to the main menu")
    try:
        if "" in main_menu:
            start_screen()
    except ValueError:
        print("Invalid input")              


class Chips:
    """
    Gives users chips to play game and adds and deducts chips per bet
    """ 

    def __init__(self, chip_balance=500):
        self.chip_balance = chip_balance
        self.current_bet = 0

    def win_bet(self):
        """
        If bet won adds balance to current balance
        """
        self.chip_balance += self.current_bet

    def lose_bet(self):
        """
        If bet lost deducts from current balance
        """
        self.chip_balance -= self.current_bet                 


def bet(chips):
    """
    Function for user to input how many chips they want to bet
    """
    while True:
        try:
            chips.current_bet = int(input("\nPlease enter your bet amount \n"))
        except ValueError:
            print("Please type a valid bet amount")
        else:
            if chips.current_bet > chips.chip_balance:
                print("You dont have enough chips to place that bet")
            elif chips.current_bet < 1:
                print("Please type a valid bet amount")
            else:
                break    
    

player_chips = Chips()            
start_screen()











