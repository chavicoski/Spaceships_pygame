"""API to setup and run the game."""
import pygame

from .config import FPS
from .classes.game_context import GameContext
from .game_utils import (setup_display, create_spaceships, handle_event,
                         update_window, handle_movement_keys, create_barrier,
                         handle_bullets)


def setup_game() -> GameContext:
    """Initializes all the objects to start the game.

    Returns:
        context: GameContext object with the context variables of the game.
    """
    game_window = setup_display()
    barrier = create_barrier()
    left_spaceship, right_spaceship = create_spaceships()
    context = GameContext(
        game_window=game_window,
        barrier=barrier,
        left_spaceship=left_spaceship,
        right_spaceship=right_spaceship,
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
            else:
                handle_event(context, event)

        handle_bullets(context)

        handle_movement_keys(context)

        update_window(context)
