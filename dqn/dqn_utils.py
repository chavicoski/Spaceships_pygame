"""Module of helper functions for the API to manage the game environment for DQN."""
import random
from typing import Tuple

import numpy as np
import pygame
from pygame.surface import Surface

from utils.config import RIGHT_LEFT, RIGHT_RIGHT, RIGHT_UP, RIGHT_DOWN, RIGHT_SHOOT
from utils.config import SPACESHIP_WIDTH, SPACESHIP_HEIGHT
from utils.config import BARRIER_WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT
from utils.config import LEFT_SPACESHIP_FILE, RIGHT_SPACESHIP_FILE
from utils.config import DISPLAY_NAME
from utils.config import RED, BG_COLOR
from utils.config import MAX_ACTIVE_BULLETS
from utils.game_utils import handle_right_spaceship_movement
from utils.game_utils import handle_bullets_fired, handle_bullets_movement, handle_bullet_hit
from utils.classes.spaceship import Spaceship
from utils.classes.bullet import Bullet
from utils.classes.game_context import GameContext
from utils.my_events import LEFT_HIT


# To control the right spaceship
N_KEYS = 512  # From len(pygame.key.get_pressed())
ACTIONS_TO_KEYS = {0: RIGHT_SHOOT,
                   1: RIGHT_LEFT,
                   2: RIGHT_RIGHT,
                   3: RIGHT_UP,
                   4: RIGHT_DOWN}


def create_random_spaceships(space_size: Tuple[int, int]) -> Tuple[Spaceship, Spaceship]:
    """Creates the spaceships objects of both sides in random locations.

    Args:
        space_size: The dimensions of the screen.

    Returns:
        A tuple with spaceships objects -> (left_spaceship, right_spaceship).
    """
    # Note: The spaceship object is rotated 90 degrees at creation
    left_init_x = random.randint(
        0, WINDOW_WIDTH // 2 - BARRIER_WIDTH // 2 - SPACESHIP_HEIGHT)
    left_init_y = random.randint(0, WINDOW_HEIGHT - SPACESHIP_WIDTH)
    left_spaceship = Spaceship(
        image_file=LEFT_SPACESHIP_FILE,
        side="left",
        init_pos=(left_init_x, left_init_y),
        name="Yellow")
    right_init_x = random.randint(
        WINDOW_WIDTH // 2 + BARRIER_WIDTH // 2, WINDOW_WIDTH - SPACESHIP_HEIGHT)
    right_init_y = random.randint(0, WINDOW_HEIGHT - SPACESHIP_WIDTH)
    right_spaceship = Spaceship(
        image_file=RIGHT_SPACESHIP_FILE,
        side="right",
        init_pos=(right_init_x, right_init_y),
        name="Red")

    return (left_spaceship, right_spaceship)


def handle_action(context: GameContext, action: np.array) -> None:
    """Performs an action.

    Args:
        context: GameContext object with the context variables of the game.
        action: A numpy with the code of the action to perform.
    """
    for event in pygame.event.get():
        handle_bullet_hit(context, event)

    if action > 0:  # Is a movement action
        keys = [False] * N_KEYS
        keys[ACTIONS_TO_KEYS[int(action)]] = True
        handle_right_spaceship_movement(context, keys)
    else:  # action=0 for shooting action
        handle_bullets_fired(context, pygame.event.Event(
            pygame.KEYDOWN, key=RIGHT_SHOOT))

    handle_bullets_movement(context)
