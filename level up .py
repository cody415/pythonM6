import pygame
import random
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 48

# Initialize Pygame
pygame.init()

# Load background image
background_image = pygame.transform.scale(
    pygame.image.load("bg.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Font
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

# Custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Colors
COLORS = [pygame.Color('red'), pygame.Color('green'),
          pygame.Color('blue'), pygame.Color('yellow'),
          pygame.Color('magenta'), pygame.Color('orange')]


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change,
                              SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change,
                              SCREEN_HEIGHT - self.rect.height), 0)

    def change_color(self):
        new_color = random.choice(COLORS)
        self.image.fill(new_color)


# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Create sprites
sprite1 = Sprite(pygame.Color('black'), 40, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)

sprite2 = Sprite(pygame.Color('red'), 40, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)

# Group
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop variables
running, won = True, False
score = 0
clock = pygame.time.Clock()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

        if won and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Reset game
            won = False
            score = 0
            all_sprites.add(sprite2)

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))
            all_sprites.remove(sprite2)
            score += 1
            won = True

    # Drawing
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, pygame.Color('black'))
    screen.blit(score_text, (10, 10))

    # Win message
    if won:
        win_text = font.render("You win! Press R to restart", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
                               (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame
