"""Module with helper internal functions for the game"""
import os

import pygame
from pygame import Rect, Surface

from .game_context import GameContext
from .config import BLACK
from .config import (VEL, YELL_LEFT, YELL_RIGHT, YELL_UP, YELL_DOWN,
                     RED_LEFT, RED_RIGHT, RED_UP, RED_DOWN)
from .config import (WINDOW_WIDTH, WINDOW_HEIGHT, BARRIER_WIDTH, DISPLAY_NAME, BG_COLOR,
                     ASSETS_PATH, YELLOW_INIT_X, YELLOW_INIT_Y, RED_INIT_X, RED_INIT_Y,
                     YELLOW_SPACESHIP_FILE, RED_SPACESHIP_FILE, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


def setup_display() -> Surface:
    """Creates the window for the game.

    Returns:
        game_window: The Surface object with the game window.
    """
    game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(DISPLAY_NAME)
    game_window.fill(BG_COLOR)
    pygame.display.update()

    return game_window


def create_barrier() -> Rect:
    """Creates a barrier with a rectangle in the middle of the screen.

    Returns:
        A Rect object that references to the created barrier.
    """
    return pygame.Rect(WINDOW_WIDTH/2 - BARRIER_WIDTH/2, 0, BARRIER_WIDTH, WINDOW_HEIGHT)


def create_spaceships() -> tuple[Surface, Surface, Rect, Rect]:
    """Creates the spaceships images and rectangle objects.

    Returns:
        A tuple the spaceships objects -> (yell_img, red_img, yell_rect, red_img).
    """
    # YELLOW SPACESHIP
    yellow_spaceship_image = pygame.image.load(
        os.path.join(ASSETS_PATH, YELLOW_SPACESHIP_FILE))
    yellow_spaceship = pygame.transform.scale(
        yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 90)
    yellow_rect = pygame.Rect(YELLOW_INIT_X, YELLOW_INIT_Y,
                              SPACESHIP_HEIGHT, SPACESHIP_WIDTH)  # Invert width and height because the image is rotated

    # RED SPACESHIP
    red_spaceship_image = pygame.image.load(
        os.path.join(ASSETS_PATH, RED_SPACESHIP_FILE))
    red_spaceship = pygame.transform.scale(
        red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    red_spaceship = pygame.transform.rotate(red_spaceship, -90)
    red_rect = pygame.Rect(RED_INIT_X, RED_INIT_Y,
                           SPACESHIP_HEIGHT, SPACESHIP_WIDTH)  # Invert width and height because the image is rotated

    return (yellow_spaceship, red_spaceship, yellow_rect, red_rect)


def update_window(context: GameContext) -> None:
    """Refreshes the displayed window using the data of the context object.

    Args:
        context: GameContext object with the context variables of the game.
    """
    context.game_window.fill(BG_COLOR)
    pygame.draw.rect(context.game_window, BLACK, context.barrier)
    pygame.draw.rect(context.game_window, BLACK, context.yellow_rect)
    pygame.draw.rect(context.game_window, BLACK, context.red_rect)
    context.game_window.blit(context.yellow_spaceship,
                             (context.yellow_rect.x, context.yellow_rect.y))
    context.game_window.blit(context.red_spaceship,
                             (context.red_rect.x, context.red_rect.y))
    pygame.display.update()


def handle_yellow_movement(context: GameContext, pressed_keys: list[bool]) -> None:
    """Handles the movement of the yellow spaceship from the pressed keys.

    Args:
        context: GameContext object with the context variables of the game.
        pressed_keys: A pygame.key.ScancodeWraper with the info about the current pressed keys.
    """
    yell_x, yell_y = context.yellow_rect.x, context.yellow_rect.y
    if pressed_keys[YELL_LEFT] and yell_x - VEL > 0:
        context.yellow_rect.x -= VEL
    if pressed_keys[YELL_RIGHT] and yell_x + VEL + context.yellow_rect.width < context.barrier.x:
        context.yellow_rect.x += VEL
    if pressed_keys[YELL_UP] and yell_y - VEL > 0:
        context.yellow_rect.y -= VEL
    if pressed_keys[YELL_DOWN] and yell_y + VEL + context.yellow_rect.height < context.game_window.get_height():
        context.yellow_rect.y += VEL


def handle_red_movement(context: GameContext, pressed_keys: list[bool]) -> None:
    """Handles the movement of the red spaceship from the pressed keys.

    Args:
        context: GameContext object with the context variables of the game.
        pressed_keys: A pygame.key.ScancodeWraper with the info about the current pressed keys.
    """
    red_x, red_y = context.red_rect.x, context.red_rect.y
    if pressed_keys[RED_LEFT] and red_x - VEL > context.barrier.x + context.barrier.width:
        context.red_rect.x -= VEL
    if pressed_keys[RED_RIGHT] and red_x + VEL + context.red_rect.width < context.game_window.get_width():
        context.red_rect.x += VEL
    if pressed_keys[RED_UP] and red_y - VEL > 0:
        context.red_rect.y -= VEL
    if pressed_keys[RED_DOWN] and red_y + VEL + context.red_rect.height < context.game_window.get_height():
        context.red_rect.y += VEL


def handle_input_keys(context: GameContext) -> None:
    """Handles the acctions to do from the current pressed keys.

    Args:
        context: GameContext object with the context variables of the game.
    """
    pressed_keys = pygame.key.get_pressed()
    handle_yellow_movement(context, pressed_keys)
    handle_red_movement(context, pressed_keys)
