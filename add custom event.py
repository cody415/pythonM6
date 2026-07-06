import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400

# Define colors
COLORS = [pygame.Color('red'), pygame.Color('green'),
          pygame.Color('blue'), pygame.Color('yellow'),
          pygame.Color('magenta'), pygame.Color('orange')]

# Custom event ID
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1


# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.color = color

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change,
                              SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change,
                              SCREEN_HEIGHT - self.rect.height), 0)

    def change_color(self):
        self.color = random.choice(COLORS)
        self.image.fill(self.color)


# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Event")

# Create sprites
sprite1 = Sprite(pygame.Color('dodgerblue'), 40, 30)
sprite1.rect.x, sprite1.rect.y = 100, 100

sprite2 = Sprite(pygame.Color('black'), 40, 30)
sprite2.rect.x, sprite2.rect.y = 300, 200

# Group sprites
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Trigger custom event with SPACE key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))

        # Handle custom event
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Movement controls for sprite1
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    sprite1.move(x_change, y_change)

    # Drawing
    screen.fill(pygame.Color('lightblue'))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
