from src.player.player import Player

class BasicStrategyAgent(Player):
    def __init__(self, deck, name="Basic AI", bankroll=100):
        super().__init__(name, bankroll)
        self.deck = deck #The deck object is stored here

    def get_action(self, hand, dealer_upcard):
        #Implement Basic BlackJack Strategy
        hand_value = hand.get_value()
        if hand_value <= 11:
            return 'h' #always hit on 11 or less
        if hand_value == 12 and dealer_upcard.value in [4, 5, 6]:
            return 's' #stand when dealer shows 4-6
        if hand_value in [13, 14, 15, 16] and dealer_upcard.value in [2, 3, 4, 5, 6]:
            return 's' #stand when dealer shows 2-6
        else:
            return 'h' #otherwise, hit