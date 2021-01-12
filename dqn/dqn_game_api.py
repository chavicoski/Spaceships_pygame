"""API to manage the game environment for DQN."""
from PIL import Image
import numpy as np
import pygame
from tf_agents.trajectories import time_step

from utils.game_utils import handle_event, handle_bullets_movement
from utils.game_utils import setup_display, update_window
from utils.game_utils import create_barrier
from utils.classes.game_context import GameContext
from dqn.dqn_utils import create_random_spaceships, handle_action


def init_game() -> GameContext:
    """Initializes a game with the spaceships at random positons.

    Returns:
        The GameContext object of the game.
    """
    game_window = setup_display()
    barrier = create_barrier()
    left_spaceship, right_spaceship = create_random_spaceships(
        (game_window.get_width(),
         game_window.get_height()))
    context = GameContext(
        game_window=game_window,
        barrier=barrier,
        left_spaceship=left_spaceship,
        right_spaceship=right_spaceship)

    return context


def reset_game(context: GameContext) -> GameContext:
    """Resets the game context with new spaceships positions.

    Args:
        context: The game context to reset.

    Returns:
        The new reseted game context.
    """
    left_spaceship, right_spaceship = create_random_spaceships(
        (context.game_window.get_width(),
         context.game_window.get_height()))
    context.restart(left_spaceship, right_spaceship)
    return context


def get_game_screenshot(context: GameContext) -> np.array:
    """Takes a screenshot of the current state of the game.

    Args:
        context: GameContext object with the context variables of the game.

    Returns:
        A numpy array with shape (W, H, 3) and normalized between [0, 1].
    """
    screen_str = pygame.image.tostring(context.game_window, "RGB")
    pil_image = Image.frombytes("RGB",
                                (context.game_window.get_width(),
                                    context.game_window.get_height()),
                                screen_str)

    res = np.asarray(pil_image) / 255.0
    return np.transpose(res, (1, 0, 2))


def perform_game_action(context: GameContext, action: int) -> None:
    """Executes an iteration of the event loop of the game given an action to perform.

    Args:
        context: GameContext object with the context variables of the game.
        action: The action (by code) to perform in the loop iteration.
    """
    handle_action(context, action)  # Perform the action in the game

    handle_bullets_movement(context)

    update_window(context)
