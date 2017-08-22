

'''
Blackjack game as Python practice
 author A. Z. Quwatli
'''

import random

playing = False
chipPool = 100
bet = 1
restart = "D to deal cards or Q to quit"
result = ""

suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

'''Card Class'''


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def print_card(self):
        print(self.suit + self.rank)


'''Hand Class'''


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        composition = " "
        for card in self.cards:
            card_name = card.__str__()
            composition += " " + card_name
        return composition + " in hand"

    def add_card(self, card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += val[card.rank]

    def hand_value(self):
        if self.ace is True and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):

        if hidden is True and playing is True:
                starting_card = 1
        else:
                starting_card = 0

        for x in range(starting_card, len(self.cards)):
                self.cards[x].print_card()


'''Deck Class'''


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        composition = " "
        for card in self.cards:
            composition += " " + card.__str__()
        return composition + " in deck"


'''Body Of Game'''


def intro():
    print("Hi! welcome to Blackjack! this game is created in Python for your pleasure!\n"
          "it is worth noting however, that I, A. Z., the author of this program, created this game"
          " while not having a single clue of what the rules nor the logic are!\n"
          "this is purely Python OOP practice\n"
          "thanx extended to Jose, my python mentor, for providing the basic code through his course so I could"
          " extract the game logic without bothering to know what the game is as I have never played a card game"
          " nor will I ever will! BATTLFIELD 1 FTW :D"
          "\nFinal note, screw Jupyter notebook, long live Pycharm\nEnjoy your game!")


def make_bet():
    global bet
    bet = 0

    print("Please enter bet amount in complete integer")

    while bet == 0:
        bet_comp = int(input())

        if 1 <= bet_comp <= chipPool:
            bet = bet_comp
        else:
            print("chips insufficient, you have {chips} remaining in pool".format(chips=chipPool))


def deal_cards():
    global result, playing, deck, player_hand, dealer_hand, chipPool, bet

    deck = Deck()

    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    result = "H to hit or S to stand "

    if playing:
        print("FOLD!")
        chipPool -= bet

    playing = True
    game_step()


def hit():
    global playing, chipPool, deck, player_hand, dealer_hand, result, bet

    if playing:
        if player_hand.hand_value() <= 21:
            player_hand.add_card(deck.deal())

    print("Player hand is  {playerHand}".format(playerHand=player_hand))

    if player_hand.hand_value() > 21:
        result = "BUSTeD!" + restart
        chipPool -= bet
        playing = False
    else:
        result = " Can't hit " + restart

    game_step()


def stand():
    global playing, chipPool, deck, player_hand, dealer_hand, result, bet

    if not playing:
        if player_hand.hand_value() > 0:
            result = "You can't stand!"

        else:
            while dealer_hand.hand_value() < 17:
                dealer_hand.add_card(deck.deal())

            if dealer_hand.hand_value() > 21:
                result = "Dealer lost! player wins!" + restart
                chipPool += bet
                playing = False
            elif dealer_hand.hand_value() < player_hand.hand_value():
                result = "Player beats dealer!" + restart
                chipPool += bet
                playing = False
            elif player_hand.hand_value() == dealer_hand.hand_value():
                result = "It's a tie! " + restart
                playing = False
            else:
                result = " Dealer wins!" + restart
                chipPool -= bet
                playing = False

    game_step()


def game_step():
    print("\nPlayer hand is: " + str(player_hand.draw(hidden=False)))

    print("Player hand total is " + str(player_hand.hand_value()))

    print("\nDealer hand is: " + str(dealer_hand.draw(hidden=True)))

    if not playing:
        print("for a total of " + str(dealer_hand.hand_value()) + "Chip Total: " + str(chipPool))

    else:
        print(" with another card hidden upside down")

    print(result)

    player_input()


def exit_game():
    print("Good Game!")
    exit()


def player_input():
    player_in = input().lower()

    if player_in == 'h':
        hit()
    elif player_in == 's':
        stand()
    elif player_in == 'd':
        deal_cards()
    elif player_in == 'q':
        exit_game()
    else:
        print("Please enter H for hit, S for stand, D for deal or Q to quit game ")
        player_input()


'''CODe tO RUN THE GAME MODULES'''

deck = Deck()
deck.shuffle()
player_hand = Hand()
dealer_hand = Hand()

intro()
deal_cards()