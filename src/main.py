from src.core.deck import Deck
from src.core.hand import Hand
from src.player.human_player import HumanPlayer
from src.player.ai.basic_strategy_agent import BasicStrategyAgent
from src.dealer.dealer import Dealer
from src.ui import ui_utils  # Import the UI utilities

def play_round(deck, player, dealer, powerups_available):
    player.hand = Hand()
    dealer.hand = Hand()

    # Players make bets
    bet_amount = player.place_bet(10)  # Placeholder bet
    ui_utils.display_message(f"{player.name} bets {bet_amount}")  # Use display_message

    # Deal initial hands
    player.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())
    player.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())

    ui_utils.display_message(f"{player.name}'s hand: {player.hand} (Value: {player.hand.get_value()})")  # Use display_message
    ui_utils.display_message(f"Dealer's up card: {dealer.hand.cards[0]}")  # Use display_message

    # Player's turn
    while player.hand.get_value() < 21:
        action = player.get_action(player.hand, dealer.hand.cards[0])  # Updated to remove powerups_available
        if isinstance(player, HumanPlayer):
            action = ui_utils.get_player_action("(H)it or (S)tand? ")
        else:
            action = player.get_action(player.hand, dealer.hand.cards[0])  # Use get_player_action

        if action == 'h':
            player.hand.add_card(deck.deal())
            ui_utils.display_message(f"{player.name} hits. Hand: {player.hand} (Value: {player.hand.get_value()})")  # Use display_message
        elif action == 's':
            ui_utils.display_message(f"{player.name} stands.")  # Use display_message
            break
        elif action == 'shuffle_up' and powerups_available['shuffle_up']:
            # Implement shuffle up Logic
            ui_utils.display_message(f"{player.name} uses Shuffle Up!")  # Use display_message
            deck = Deck()  # recreate the deck
            player.hand = Hand()
            player.hand.add_card(deck.deal())
            player.hand.add_card(deck.deal())
            powerups_available['shuffle_up'] = False  # Player has used it.
            ui_utils.display_message(f"{player.name}'s hand: {player.hand} (Value: {player.hand.get_value()})")  # Use display_message

        elif action == 'peek' and powerups_available['peek']:
            ui_utils.display_message(f"{player.name} uses Peek!")  # Use display_message
            ui_utils.display_message(f"Dealer's hand: {dealer.hand} (Value: {dealer.hand.get_value()})")  # Use display_message
            powerups_available['peek'] = False
        elif action == 'perfect_swap' and powerups_available['perfect_swap']:
            ui_utils.display_message(f"{player.name} uses Perfect Swap!")  # Use display_message
            # For now, just swap the first card.
            card_to_swap = player.hand.cards[0]
            player.hand.cards.remove(card_to_swap)
            new_card = deck.deal()
            player.hand.add_card(new_card)
            powerups_available['perfect_swap'] = False
            ui_utils.display_message(f"{player.name}'s hand: {player.hand} (Value: {player.hand.get_value()})")  # Use display_message
        else:
            ui_utils.display_message("Invalid Action")  # Use display_message

    if player.hand.get_value() > 21:
        ui_utils.display_message(f"{player.name} busts!")  # Use display_message
        return

    # Dealer's turn
    ui_utils.display_message(f"Dealer's hand: {dealer.hand} (Value: {dealer.hand.get_value()})")  # Use display_message
    while dealer.hand.get_value() < 17:
        action = dealer.get_action(dealer.hand)
        if action == 'h':
            dealer.hand.add_card(deck.deal())
            ui_utils.display_message(f"Dealer hits. Hand: {dealer.hand} (Value: {dealer.hand.get_value()})")  # Use display_message
        else:
            ui_utils.display_message("Dealer stands.")  # Use display_message
            break

    if dealer.hand.get_value() > 21:
        ui_utils.display_message("Dealer busts!")  # Use display_message
        player.receive_winnings(bet_amount * 2)  # Player gets initial bet back, plus winnings
        ui_utils.display_message(f"{player.name} wins! Bankroll: {player.bankroll}")  # Use display_message
        return

    # Determine the winner
    if player.hand.get_value() > dealer.hand.get_value():
        ui_utils.display_message(f"{player.name} wins!")  # Use display_message
        player.receive_winnings(bet_amount * 2)
        ui_utils.display_message(f"{player.name}'s Bankroll: {player.bankroll}")  # Use display_message
    elif player.hand.get_value() == dealer.hand.get_value():
        ui_utils.display_message("Push!")  # Use display_message
        player.receive_winnings(bet_amount)  # Return original bet
        ui_utils.display_message(f"{player.name}'s Bankroll: {player.bankroll}")  # Use display_message
    else:
        ui_utils.display_message("Dealer wins!")  # Use display_message


if __name__ == "__main__":
    deck = Deck(num_decks=2)  # Create the deck
    player = HumanPlayer("Alice", 100)  # Create a player
    dealer = Dealer()  # Create a dealer

    powerups_available = {
        'shuffle_up': True,
        'peek': True,
        'perfect_swap': True  # Added Perfect Swap
    }

    play_round(deck, player, dealer, powerups_available)
