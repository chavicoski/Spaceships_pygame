"""API to setup and run the game."""
import pygame

from .config import FPS
from .game_utils import (setup_display, create_spaceships,
                         update_window, handle_input_keys, create_barrier)
from .game_context import GameContext


def setup_game() -> GameContext:
    """Initializes all the objects to start the game.

    Returns:
        context: GameContext object with the context variables of the game.
    """
    game_window = setup_display()
    barrier = create_barrier()
    yellow_spaceship, red_spaceship, yellow_rect, red_rect = create_spaceships()
    context = GameContext(
        game_window=game_window,
        barrier=barrier,
        yellow_spaceship=yellow_spaceship,
        red_spaceship=red_spaceship,
        yellow_rect=yellow_rect,
        red_rect=red_rect
    )

    return context


def game_loop(context: GameContext) -> None:
    """Executes the event loop that runs the game.

    Args:
        context: GameContext object with the context variables of the game.
    """
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        handle_input_keys(context)

        update_window(context)