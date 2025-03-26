class Player:
    def __init__(self, name, bankroll=100):
        self.name = name
        self.hand = None
        self.bankroll = bankroll

    def place_bet(self, amount):
        if amount > 0 and amount <= self.bankroll:
            self.bankroll -= amount
            return amount
        else:
            return 0  # Invalid bet

    def receive_winnings(self, amount):
        self.bankroll += amount

    def __str__(self):
        return f"{self.name} (Bankroll: {self.bankroll})"