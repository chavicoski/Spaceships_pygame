"""Global settings of the game."""
import pygame

#  SETTINGS
FPS = 144
VEL = 5
BULLET_VEL = 7

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500

BARRIER_WIDTH = WINDOW_WIDTH * 0.05

SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

YELLOW_INIT_X = 300
YELLOW_INIT_Y = 100

RED_INIT_X = 700
RED_INIT_Y = 100

# CONTROLS
YELL_LEFT = pygame.K_a
YELL_RIGHT = pygame.K_d
YELL_UP = pygame.K_w
YELL_DOWN = pygame.K_s

RED_LEFT = pygame.K_j
RED_RIGHT = pygame.K_l
RED_UP = pygame.K_i
RED_DOWN = pygame.K_k

#RED_LEFT = pygame.K_LEFT
#RED_RIGHT = pygame.K_RIGHT
#RED_UP = pygame.K_UP
#RED_DOWN = pygame.K_DOWN

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# PATHS
ASSETS_PATH = "assets"
YELLOW_SPACESHIP_FILE = "spaceship_yellow.png"
RED_SPACESHIP_FILE = "spaceship_red.png"

# METADATA
DISPLAY_NAME = "First Game"
BG_COLOR = WHITE
