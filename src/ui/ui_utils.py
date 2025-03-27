def get_player_action(prompt):
    """Gets player action from the UI (currently console-based)."""
    return input(prompt).lower()


def display_message(message):
    """Displays a message to the UI (currently console-based)."""
    print(message)