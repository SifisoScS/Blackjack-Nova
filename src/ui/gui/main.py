import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Blackjack Nova")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 128, 0))  # Green background

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()