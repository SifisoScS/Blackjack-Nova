import random
from src.core import game_logic
from src.core import card

class PowerUpAdvisor:
    def __init__(self, deck, player_hand, dealer_upcard):
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_upcard = dealer_upcard

    def _evaluate_peek(self):
        """Roughly estimate the value of peeking."""
        # Very basic heuristic: Does knowing the dealer's hand make a big
        # difference right now?
        dealer_likely_bust = self.dealer_upcard.value >= 7
        if dealer_likely_bust:
            return 0.1  # Slight positive, better to know
        return -0.05 # Small negative otherwise
    def _evaluate_shuffle_up(self):
        """Check to see if the player's hand would benefit from shuffling up."""
        expected_value = game_logic.calculate_hand_value(self.player_hand)
        #Check whether player's cards are already good
        #TODO: Write this logic
        if expected_value > 12:
          return 0
        return 0.1 #Otherwise its beneficial to shuffle up
    def _evaluate_perfect_swap(self):
        """Estimates the value of using Perfect Swap."""
        hand_value = game_logic.calculate_hand_value(self.player_hand)
        if hand_value >= 17:  #Don't swap a good hand
            return 0

        worst_card = None
        worst_card_value = 20 #Large
        for card in self.player_hand.cards:
          if card.value < worst_card_value:
              worst_card = card
              worst_card_value = card.value
        if worst_card is None:
          return 0 #No card can be "worse"

        #Very simple "better card" logic:
        remaining_cards = len(self.deck.cards)
        cards_better_than_worst = 0
        for card in self.deck.cards:
          if card.value > worst_card.value:
              cards_better_than_worst += 1
        #Adjust evaluation depending on how many cards remain
        if remaining_cards < 10:
          return 0
        probability_better = cards_better_than_worst/remaining_cards

        return probability_better * 0.2 #Return Evaluation