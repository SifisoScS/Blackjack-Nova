from src.core.deck import Deck
from src.core.hand import Hand
from src.player.human_player import HumanPlayer
from src.player.ai.basic_strategy_agent import BasicStrategyAgent
from src.dealer.dealer import Dealer

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.deck import Deck

def play_round(deck, player, dealer, powerups_available):
  player.hand = Hand()
  dealer.hand = Hand()

  #Players make bets
  bet_amount = player.place_bet(10) #Placeholder bet
  print(f"{player.name} bets {bet_amount}")

  #Deal initial hands
  player.hand.add_card(deck.deal())
  dealer.hand.add_card(deck.deal())
  player.hand.add_card(deck.deal())
  dealer.hand.add_card(deck.deal())

  print(f"{player.name}'s hand: {player.hand} (Value: {player.hand.get_value()})")
  print(f"Dealer's up card: {dealer.hand.cards[0]}")

  #Player's turn
  while player.hand.get_value() < 21:
      action = player.get_action(player.hand, dealer.hand.cards[0])

      if action == 'h':
          player.hand.add_card(deck.deal())
          print(f"{player.name} hits. Hand: {player.hand} (Value: {player.hand.get_value()})")
      elif action == 's':
          print(f"{player.name} stands.")
          break
      elif action == 'shuffle_up' and powerups_available['shuffle_up']:
            #Implement shuffle up Logic
            print(f"{player.name} uses Shuffle Up!")
            deck = Deck() #recreate the deck
            player.hand = Hand()
            player.hand.add_card(deck.deal())
            player.hand.add_card(deck.deal())
            powerups_available['shuffle_up'] = False #Player has used it.
            print(f"{player.name}'s hand: {player.hand} (Value: {player.hand.get_value()})")

      elif action == 'peek' and powerups_available['peek']:
        print(f"{player.name} uses Peek!")
        print(f"Dealer's hand: {dealer.hand} (Value: {dealer.hand.get_value()})")
        powerups_available['peek'] = False
      elif action == 'perfect_swap' and powerups_available['perfect_swap']:
        print(f"{player.name} uses Perfect Swap!")
        #For now, just swap the first card.
        card_to_swap = player.hand.cards[0]
        player.hand.cards.remove(card_to_swap)
        new_card = deck.deal()
        player.hand.add_card(new_card)
        powerups_available['perfect_swap'] = False
        print(f"{player.name}'s hand: {player.hand} (Value: {player.hand.get_value()})")
      else:
        print("Invalid Action")

  if player.hand.get_value() > 21:
      print(f"{player.name} busts!")
      return

  #Dealer's turn
  print(f"Dealer's hand: {dealer.hand} (Value: {dealer.hand.get_value()})")
  while dealer.hand.get_value() < 17:
      action = dealer.get_action(dealer.hand)
      if action == 'h':
          dealer.hand.add_card(deck.deal())
          print(f"Dealer hits. Hand: {dealer.hand} (Value: {dealer.hand.get_value()})")
      else:
          print("Dealer stands.")
          break

  if dealer.hand.get_value() > 21:
      print("Dealer busts!")
      player.receive_winnings(bet_amount * 2) #Player gets initial bet back, plus winnings
      print(f"{player.name} wins! Bankroll: {player.bankroll}")
      return

  #Determine the winner
  if player.hand.get_value() > dealer.hand.get_value():
      print(f"{player.name} wins!")
      player.receive_winnings(bet_amount * 2)
      print(f"{player.name}'s Bankroll: {player.bankroll}")
  elif player.hand.get_value() == dealer.hand.get_value():
      print("Push!")
      player.receive_winnings(bet_amount) #Return original bet
      print(f"{player.name}'s Bankroll: {player.bankroll}")
  else:
      print("Dealer wins!")


if __name__ == "__main__":
    deck = Deck(num_decks=2) #Create the deck
    player = HumanPlayer("Alice", 100) #Create a player
    dealer = Dealer() #Create a dealer

    powerups_available = {
        'shuffle_up': True,
        'peek': True,
        'perfect_swap': True  # Added Perfect Swap
    }

    play_round(deck, player, dealer, powerups_available)
