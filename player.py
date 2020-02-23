
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_a_card(self, card):
        self.hand.append(card)
    
    def hello(self):
        print("Hello, my name is", self.name)
    
    def get_hand_total(self):
        total = 0
        for card in self.hand:
            if card.value in ["J", "Q", "K"]:
                total += 10
            elif card.value == "ACE":
                total += 1
            else:
                total += int(card.value)
        return total % 10