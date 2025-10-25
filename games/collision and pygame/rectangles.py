import pygame
import random
# Constants for easier adjustments
SCREEN_WIDTH,  SCREEN_HEIGHT = 800, 600
MOVE_STEP = 5
# Initialize Pygame
pygame.init()
# Load and transform the background image
background_image = pygame.trasform.scale(pygame.image.load("pg.jpeg"),
                                            (SCREEN_WIDTH, SCREEN_HEIGHT))
# Load font once at the beginning
font = pygame.font.SysFont("times new roman", 70)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(0, SCREEN_WIDTH),
                            random.randint(0, SCREEN_HEIGHT)]
    def move(self, xc, yc):
        self.rect.x += xc
        self.rect.y += yc
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT- self.rect.height))
# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Collision')
clock = pygame.time.Clock()
# Create sprites
sp = pygame.sprite.Group()
sp1 = Sprite((255, 0, 0), 50, 50)
sp2 = Sprite((0, 255, 0), 50, 50)
sp.add(sp1, sp2)

all_sp = pygame.sprite.Group()
all_sp.add(sp1, sp2)

sp2.rect.x = random.randint(100, 700)
sp2.rect.y = random.randint(100, 500)

# Game loop control variables
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False


# Main game loop

  # Drawing

  # Display win message
