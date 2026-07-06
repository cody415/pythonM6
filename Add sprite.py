import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

# Colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, controllable=False):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]
        self.controllable = controllable

    def update(self, keys=None):
        if self.controllable and keys:
            # Controlled sprite movement
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
            if keys[pygame.K_UP]:
                self.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.rect.y += 5
        else:
            # Automatic bouncing movement
            self.rect.move_ip(self.velocity)
            if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
                self.velocity[0] = -self.velocity[0]
            if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
                self.velocity[1] = -self.velocity[1]


# Create sprites
auto_sprite = Sprite(YELLOW, 40, 30)   # Moves automatically
auto_sprite.rect.x = random.randint(0, SCREEN_WIDTH - 40)
auto_sprite.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

player_sprite = Sprite(MAGENTA, 40, 30, controllable=True)  # Controlled by keys
player_sprite.rect.x = SCREEN_WIDTH // 2
player_sprite.rect.y = SCREEN_HEIGHT // 2

# Group sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(auto_sprite)
all_sprites.add(player_sprite)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites Game")

# Background color
bg_color = LIGHTBLUE

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update sprites
    auto_sprite.update()
    player_sprite.update(keys)

    # Draw everything
    screen.fill(bg_color)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
