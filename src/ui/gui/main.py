import pygame
from src.core.deck import Deck  # Import Deck for testing
from src.core.hand import Hand  # Import Hand for testing
from src.core.card import Card #Import Card for testing

# Initialize Pygame
pygame.init()

# Set window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Blackjack Nova")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Card dimensions
card_width = 70
card_height = 100

def draw_card(screen, card, x, y):
    """Draws a card as a rectangle with text."""
    pygame.draw.rect(screen, WHITE, (x, y, card_width, card_height))
    font = pygame.font.Font(None, 16)  # Default font, size 16 (Changed from 30)
    text = font.render(str(card), True, BLACK) #Card String
    text_rect = text.get_rect(center=(x + card_width // 2, y + card_height // 2))
    screen.blit(text, text_rect)

# Game loop
running = True
#Create a sample hand for testing
deck = Deck()
hand = Hand()
hand.add_card(deck.deal())
hand.add_card(deck.deal())

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 128, 0))  # Green background

    # Draw the hand
    card_x = 50
    card_y = 100
    for card in hand.cards:
        draw_card(screen, card, card_x, card_y)
        card_x += card_width + 10  # Add spacing between cards

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()