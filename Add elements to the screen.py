# Game screen with rectangle and text using Pygame

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen with Shapes & Text")

# Define colors (RGB format)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up font
font = pygame.font.SysFont("Arial", 36)

# Create text surface
text_surface = font.render("Welcome to My Game!", True, BLACK)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw a rectangle (x, y, width, height)
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))

    # Draw
