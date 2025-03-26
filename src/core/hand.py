class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        #Basic hand calculation: can be improved
        total = 0
        aces = 0
        for card in self.cards:
            if card.rank != 'A':
                total += card.value
            else:
                aces+=1
                total += 11
        while total > 21 and aces > 0:
          total -= 10
          aces -= 1
        return total

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)