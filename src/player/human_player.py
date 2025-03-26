from src.player.player import Player

class HumanPlayer(Player):
    def __init__(self, name, bankroll=100):
        super().__init__(name, bankroll)

    def get_action(self, hand, dealer_upcard):
        # Get hit or stand decision from user input
        while True:
            action = input("(H)it or (S)tand? ").lower()
            if action in ('h', 's'):
                return action
            else:
                print("Invalid input. Please enter 'H' or 'S'.")