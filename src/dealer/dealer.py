from src.player.player import Player
from src.core import game_logic

class Dealer(Player):
    def __init__(self, name="Dealer", bankroll = 100000000): #Dealers bank roll is basically infinte
        super().__init__(name, bankroll)

    def get_action(self, hand):
        #Basic dealer strategy: hit below 17, stand on 17 or above
        hand_value = game_logic.calculate_hand_value(hand)
        if hand_value < 17:
            return 'h'
        else:
            return 's'