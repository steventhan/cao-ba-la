from player import Player
from deck import Deck
from random import shuffle

"""

Methods:
    __init__(): a.k.a constructor
    start(): is used to start the game
"""
class Game:
    # def __init__(self, game_name, player1, player2):
    #     self.game_name = game_name
    #     self.player1 = player1
    #     self.player2 = player2

    def __init__(self, game_name):
        self.game_name = game_name
        self.player1 = Player("Steven")
        self.player2 = Player("Kelly")
        self.deck = Deck()
        shuffle(self.deck.cards)

    def start(self):
        print(self.game_name + " is starting")
        self.player1.hello()
        self.player2.hello()
        # Deal 3 cards for each player
        print(self.deck)
        for _ in range(3):
            self.player1.add_a_card(self.deck.draw_a_card())
            self.player2.add_a_card(self.deck.draw_a_card())
        print(self.player1.hand)
        print(self.player2.hand)
        player1_total = self.player1.get_hand_total()
        player2_total = self.player2.get_hand_total()
        print(player1_total, player2_total)

        if player1_total > player2_total:
            print(self.player1.name, "won")
        elif player2_total > player1_total:
            print(self.player2.name, "won")
        else:
            print("draw")

