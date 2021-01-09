"""Global settings of the game."""
import os

import pygame

#  SETTINGS
FPS = 60
VEL = 5
INIT_HEALTH = 10
BULLET_VEL = 7
MAX_ACTIVE_BULLETS = 3

pygame.font.init()
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
WIN_TEXT_DELAY = 5000  # 5 seconds
HP_FONT = pygame.font.SysFont('comicsans', 40)
HP_PADDING = 10

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500

BARRIER_WIDTH = WINDOW_WIDTH * 0.05

SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

LEFT_INIT_X = 300
LEFT_INIT_Y = 100

RIGHT_INIT_X = 700
RIGHT_INIT_Y = 100

# CONTROLS
LEFT_LEFT = pygame.K_a
LEFT_RIGHT = pygame.K_d
LEFT_UP = pygame.K_w
LEFT_DOWN = pygame.K_s
LEFT_SHOOT = pygame.K_LCTRL

RIGHT_LEFT = pygame.K_j
RIGHT_RIGHT = pygame.K_l
RIGHT_UP = pygame.K_i
RIGHT_DOWN = pygame.K_k
RIGHT_SHOOT = pygame.K_RCTRL

#RIGHT_LEFT = pygame.K_LEFT
#RIGHT_RIGHT = pygame.K_RIGHT
#RIGHT_UP = pygame.K_UP
#RIGHT_DOWN = pygame.K_DOWN

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# PATHS
ASSETS_PATH = "assets"
BACKGROUND_IMAGE_FILE = "space.png"
LEFT_SPACESHIP_FILE = "spaceship_yellow.png"
RIGHT_SPACESHIP_FILE = "spaceship_red.png"

# METADATA
DISPLAY_NAME = "First Game"
BG_COLOR = BLACK

# SOUND
pygame.mixer.init()
VOLUME = 0.2  # [0, 1] range
BULLET_HIT_SOUND_FILE = "Grenade+1.mp3"
BULLET_SHOOT_SOUND_FILE = "Gun+Silencer.mp3"
BULLET_HIT_SOUND = pygame.mixer.Sound(
    os.path.join(ASSETS_PATH, BULLET_HIT_SOUND_FILE))
BULLET_SHOOT_SOUND = pygame.mixer.Sound(
    os.path.join(ASSETS_PATH, BULLET_SHOOT_SOUND_FILE))
BULLET_HIT_SOUND.set_volume(VOLUME)
BULLET_SHOOT_SOUND.set_volume(VOLUME)
