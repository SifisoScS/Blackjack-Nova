def calculate_hand_value(hand):
    # Moved from Hand class for better organization.

    total = 0
    aces = 0
    for card in hand.cards:
        if card.rank != 'A':
            total += card.value
        else:
            aces+=1
            total += 11
    while total > 21 and aces > 0:
      total -= 10
      aces -= 1
    return total