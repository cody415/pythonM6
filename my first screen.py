# First Game Screen using Pygame

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen")

# Load the image (make sure ant.png is in the same folder)
ant_image = pygame.image.load("ant.png")

# Get the rectangle of the image for positioning
ant_rect = ant_image.get_rect()
ant_rect.center = (screen_width // 2, screen_height // 2)  # Center of screen

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window
            running = False

    # Fill background with a color
    screen.fill((173, 216, 230))  # Light blue background

    # Draw the image
    screen.blit(ant_image, ant_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
