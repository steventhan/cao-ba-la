
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.suit} {self.value}"

values = "2 3 4 5 6 7 8 9 10 J Q K ACE".split()
suits = "Heart Diamond Club Spade".split()

class Deck:
    def __init__(self):
        self.cards = []
        for value in values:
            for suit in suits:
                card = Card(suit, value)
                self.cards.append(card)
    
    def draw_a_card(self):
        return self.cards.pop()

    def __repr__(self):
        return str(self.cards)