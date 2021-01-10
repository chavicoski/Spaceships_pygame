import os
from typing import Tuple

import pygame

from ..config import ASSETS_PATH, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, INIT_HEALTH


class Spaceship:
    """Class that models the spaceships objects."""

    def __init__(self,
                 image_file: str,
                 side: str,
                 init_pos: Tuple[int, int],
                 name: str = "",
                 health: int = INIT_HEALTH):
        """Spaceship constructor.

        Args:
            image_file: str with the name of the image file that represents the spaceship.
            side: str ("left" or "right") that designates the side on the field for the spaceship.
            init_pos: A tuple with the initial postition of the spaceship.
            name: The name of the spaceship.
            health: int value with the initial health of the spaceship.
        """
        # Prepare the image for the spaceship
        spaceship_surface = pygame.image.load(
            os.path.join(ASSETS_PATH, image_file))
        spaceship_surface = pygame.transform.scale(
            spaceship_surface, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
        if side == "left":
            spaceship_surface = pygame.transform.rotate(
                spaceship_surface, 90)  # Look to the right
        elif side == "right":
            spaceship_surface = pygame.transform.rotate(
                spaceship_surface, -90)  # Look to the left
        else:
            print(
                f"Error! The side name \"{side}\" is not valid to create a Spaceship.")
        self.surface = spaceship_surface

        # Rectangle body of the spaceship
        self.body = pygame.Rect(
            init_pos[0], init_pos[1], SPACESHIP_HEIGHT, SPACESHIP_WIDTH)  # Invert width and height because the surface is rotated

        self.side = side

        if name == "":
            self.name = f"{side}_spaceship"
        else:
            self.name = name

        self.health = health

    def is_dead(self) -> bool:
        """Checks if the spaceship is dead.

        Returns:
            A bool saying if the spaceship is dead.
        """
        return self.health <= 0
