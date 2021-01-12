import os
from typing import List

import pygame
from pygame.surface import Surface
from pygame import Rect

from utils.classes.bullet import Bullet
from utils.classes.spaceship import Spaceship
from utils.config import ASSETS_PATH, BACKGROUND_IMAGE_FILE
from utils.config import WINDOW_WIDTH, WINDOW_HEIGHT


class GameContext:
    """Class to handle the global variables of the game."""

    def __init__(self,
                 game_window: Surface,
                 barrier: Rect,
                 left_spaceship: Spaceship,
                 right_spaceship: Spaceship,
                 left_bullets: List[Bullet] = [],
                 right_bullets: List[Bullet] = []):
        """Context constructor.

        Args:
            game_window: Surface object of the game window.
            barrier: A Rect object that represents the middle barrier of the field.
            left_spaceship: Spaceship object from left side.
            right_spaceship: Spaceship object from right side.
            left_bullets: list with the current active bullets from left spaceship.
            right_bullets: list with the current active bullets from right spaceship.
        """
        self.game_window = game_window
        self.barrier = barrier
        self.left_spaceship = left_spaceship
        self.right_spaceship = right_spaceship
        self.left_bullets = left_bullets
        self.right_bullets = right_bullets
        # Store default background
        self.background_surface = pygame.transform.scale(
            pygame.image.load(os.path.join(
                ASSETS_PATH, BACKGROUND_IMAGE_FILE)),
            (WINDOW_WIDTH, WINDOW_HEIGHT))

    def restart(self, left_spaceship: Spaceship, right_spaceship: Spaceship) -> None:
        """Restarts the game context and sets the new pair of spaceships.

        Args:
            left_spaceship: Spaceship object from left side.
            right_spaceship: Spaceship object from right side.
        """
        self.left_spaceship = left_spaceship
        self.right_spaceship = right_spaceship
        self.left_bullets = []
        self.right_bullets = []
