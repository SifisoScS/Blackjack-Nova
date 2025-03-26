class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()

    def _get_value(self):
        if self.rank in ('J', 'Q', 'K'):
            return 10
        elif self.rank == 'A':
            return 11  # Can be adjusted later
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"