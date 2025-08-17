# n = int(input("enter the value of terms"))
# sum = 0
# i = 1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print ("\nsum = ", sum) 
# i = 0
# while True:
#     print ("I AM INVEVITABLE")
#     print ("I AM INVEVITABLE")
#     print ("I AM INVEVITABLE")
#     print ("I AM INVEVITABLE")
#     print ("I AM INVEVITABLE")
    
# num = int(input("enter a number: "))
# sum = 0
# temp = num
# digit_num = len(str(num))
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digit_num
#     temp //= 10
# if num == sum:
#     print(num, "is an armstrong number")
# else:
#     print (num, "is not an armstrong number")
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 300, 600
ROWS, COLS = 20, 10
BLOCK_SIZE = WIDTH // COLS

# Colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Grid
def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            if (j, i) in locked_positions:
                grid[i][j] = locked_positions[(j, i)]
    return grid

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation % len(self.shape)]

    def get_positions(self):
        positions = []
        shape = self.image()
        for i, line in enumerate(shape):
            for j, column in enumerate(line):
                if column:
                    positions.append((self.x + j, self.y + i))
        return positions

def convert_shape_format(piece):
    positions = []
    format = piece.image()
    for i, line in enumerate(format):
        for j, column in enumerate(line):
            if column:
                positions.append((piece.x + j, piece.y + i))
    return positions

def valid_space(piece, grid):
    accepted = [[(j, i) for j in range(COLS) if grid[i][j] == BLACK] for i in range(ROWS)]
    accepted = [j for sub in accepted for j in sub]
    formatted = convert_shape_format(piece)
    for pos in formatted:
        if pos not in accepted:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positi
