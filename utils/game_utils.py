"""Module with helper functions for the game"""
from typing import Tuple, Sequence

import pygame
from pygame import Rect
from pygame.surface import Surface

from utils.classes.game_context import GameContext
from utils.classes.bullet import Bullet
from utils.classes.spaceship import Spaceship
from utils.config import BARRIER_WIDTH
from utils.config import LEFT_SPACESHIP_FILE, RIGHT_SPACESHIP_FILE
from utils.config import WINDOW_WIDTH, WINDOW_HEIGHT, DISPLAY_NAME, BG_COLOR
from utils.config import VEL, BULLET_VEL, MAX_ACTIVE_BULLETS
from utils.config import LEFT_INIT_X, LEFT_INIT_Y, RIGHT_INIT_X, RIGHT_INIT_Y
from utils.config import LEFT_LEFT, LEFT_RIGHT, LEFT_UP, LEFT_DOWN, LEFT_SHOOT
from utils.config import RIGHT_LEFT, RIGHT_RIGHT, RIGHT_UP, RIGHT_DOWN, RIGHT_SHOOT
from utils.config import WHITE, RED, YELLOW
from utils.config import WINNER_FONT, HP_FONT, HP_PADDING, WIN_TEXT_DELAY
from utils.config import BULLET_HIT_SOUND, BULLET_SHOOT_SOUND
from utils.my_events import LEFT_HIT, RIGHT_HIT, WIN


def setup_display() -> Surface:
    """Creates the window for the game and initializes it.

    Returns:
        game_window: The Surface object with the game window.
    """
    game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(DISPLAY_NAME)
    game_window.fill(BG_COLOR)
    pygame.display.update()

    return game_window


def create_barrier() -> Rect:
    """Creates a barrier with a rectangle in the middle of the screen. This barrier
       acts as limit for each spaceship area.


    Returns:
        A Rect object that references to the created barrier.
    """
    return pygame.Rect(int(WINDOW_WIDTH / 2 - BARRIER_WIDTH / 2), 0, BARRIER_WIDTH, WINDOW_HEIGHT)


def create_spaceships() -> Tuple[Spaceship, Spaceship]:
    """Creates the spaceships objects of both sides.

    Returns:
        A tuple with spaceships objects -> (left_spaceship, right_spaceship).
    """
    left_spaceship = Spaceship(
        image_file=LEFT_SPACESHIP_FILE,
        side="left",
        init_pos=(LEFT_INIT_X, LEFT_INIT_Y),
        name="Yellow")
    right_spaceship = Spaceship(
        image_file=RIGHT_SPACESHIP_FILE,
        side="right",
        init_pos=(RIGHT_INIT_X, RIGHT_INIT_Y),
        name="Red")

    return (left_spaceship, right_spaceship)


def restart_game(context: GameContext) -> None:
    """Restarts the game by restarting the game context with new spaceships. 

    Args:
        context: GameContext object with the context variables of the game.
    """
    left_spaceship, right_spaceship = create_spaceships()
    context.restart(left_spaceship, right_spaceship)


def update_window(context: GameContext) -> None:
    """Refreshes the displayed window using the data of the context object.

    Args:
        context: GameContext object with the context variables of the game.
    """
    context.game_window.blit(context.background_surface, (0, 0))

    # Show spaceships health
    left_health_text = HP_FONT.render(
        f"HP: {context.left_spaceship.health}", True, WHITE)
    right_health_text = HP_FONT.render(
        f"HP: {context.right_spaceship.health}", True, WHITE)
    context.game_window.blit(
        left_health_text,
        (HP_PADDING, HP_PADDING))
    context.game_window.blit(
        right_health_text,
        (context.game_window.get_width() -
         right_health_text.get_width() - HP_PADDING, HP_PADDING))

    # Draw spaceships
    context.game_window.blit(context.left_spaceship.surface,
                             (context.left_spaceship.body.x, context.left_spaceship.body.y))
    context.game_window.blit(context.right_spaceship.surface,
                             (context.right_spaceship.body.x, context.right_spaceship.body.y))

    # Draw bullets
    for bullet in context.left_bullets + context.right_bullets:
        pygame.draw.rect(context.game_window, bullet.color, bullet.body)

    pygame.display.update()


def handle_left_spaceship_movement(context: GameContext, pressed_keys: Sequence[bool]) -> None:
    """Handles the movement of the left side spaceship from the pressed keys.

    Args:
        context: GameContext object with the context variables of the game.
        pressed_keys: A pygame.key.ScancodeWraper with the info about the current pressed keys.
    """
    x_pos, y_pos = context.left_spaceship.body.x, context.left_spaceship.body.y
    body_width, body_height = context.left_spaceship.body.width, context.left_spaceship.body.height
    if pressed_keys[LEFT_LEFT] and x_pos - VEL > 0:
        context.left_spaceship.body.x -= VEL
    if pressed_keys[LEFT_RIGHT] and x_pos + VEL + body_width < context.barrier.x:
        context.left_spaceship.body.x += VEL
    if pressed_keys[LEFT_UP] and y_pos - VEL > 0:
        context.left_spaceship.body.y -= VEL
    if pressed_keys[LEFT_DOWN] and y_pos + VEL + body_height < context.game_window.get_height():
        context.left_spaceship.body.y += VEL


def handle_right_spaceship_movement(context: GameContext, pressed_keys: Sequence[bool]) -> None:
    """Handles the movement of the right side spaceship from the pressed keys.

    Args:
        context: GameContext object with the context variables of the game.
        pressed_keys: A pygame.key.ScancodeWraper with the info about the current pressed keys.
    """
    x_pos, y_pos = context.right_spaceship.body.x, context.right_spaceship.body.y
    body_width, body_height = context.right_spaceship.body.width, context.right_spaceship.body.height
    if pressed_keys[RIGHT_LEFT] and x_pos - VEL > context.barrier.x + context.barrier.width:
        context.right_spaceship.body.x -= VEL
    if pressed_keys[RIGHT_RIGHT] and x_pos + VEL + body_width < context.game_window.get_width():
        context.right_spaceship.body.x += VEL
    if pressed_keys[RIGHT_UP] and y_pos - VEL > 0:
        context.right_spaceship.body.y -= VEL
    if pressed_keys[RIGHT_DOWN] and y_pos + VEL + body_height < context.game_window.get_height():
        context.right_spaceship.body.y += VEL


def handle_bullets_fired(context: GameContext, event: pygame.event.Event) -> None:
    """Handles the shooting action of the spaceships when they press the shoot key.

    Args:
        context: GameContext object with the context variables of the game.
        event: An EventType object with the current event to handle.
    """
    if event.type == pygame.KEYDOWN:
        if event.key == LEFT_SHOOT and len(context.left_bullets) < MAX_ACTIVE_BULLETS:
            context.left_bullets.append(
                Bullet(shooter=context.left_spaceship, color=YELLOW))
            BULLET_SHOOT_SOUND.play()
        elif event.key == RIGHT_SHOOT and len(context.right_bullets) < MAX_ACTIVE_BULLETS:
            context.right_bullets.append(
                Bullet(shooter=context.right_spaceship, color=RED))
            BULLET_SHOOT_SOUND.play()


def handle_bullet_hit(context: GameContext, event: pygame.event.Event) -> None:
    """Handles the damage dealt when a bullet hits an spaceship.

    Args:
        context: GameContext object with the context variables of the game.
        event: An EventType object with the current event to handle.
    """
    if event.type == RIGHT_HIT:
        context.right_spaceship.health -= event.damage
        BULLET_HIT_SOUND.play()
        if context.right_spaceship.is_dead():
            pygame.event.post(pygame.event.Event(
                WIN, winner=context.left_spaceship))
    if event.type == LEFT_HIT:
        context.left_spaceship.health -= event.damage
        BULLET_HIT_SOUND.play()
        if context.left_spaceship.is_dead():
            pygame.event.post(pygame.event.Event(
                WIN, winner=context.right_spaceship))


def handle_win(context: GameContext, event: pygame.event.Event) -> None:
    """Handles the win event, showing the winner and restarting the game.

    Args: 
        context: GameContext object with the context variables of the game.
        event: An EventType object with the current event to handle.
    """
    if event.type == WIN:
        win_text = WINNER_FONT.render(f"{event.winner.name} wins", True, WHITE)
        context.game_window.blit(
            win_text,
            (context.game_window.get_width() // 2 - win_text.get_width() // 2,
             context.game_window.get_height() // 2 - win_text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(WIN_TEXT_DELAY)  # Wait a bit in the winner screen
        restart_game(context)


def handle_event(context: GameContext, event: pygame.event.Event) -> None:
    """Event handler of the game.

    Args:
        context: GameContext object with the context variables of the game.
        event: An EventType object with the current event to handle.
    """
    handle_win(context, event)
    handle_bullet_hit(context, event)
    handle_bullets_fired(context, event)


def handle_bullets_movement(context: GameContext) -> None:
    """Handles the movement and collisions of the bullets.

    Args:
        context: GameContext object with the context variables of the game.
    """
    for bullet in context.left_bullets:
        bullet.body.x += BULLET_VEL
        if bullet.is_hitting(context.right_spaceship):
            pygame.event.post(pygame.event.Event(
                RIGHT_HIT, damage=bullet.damage))
            context.left_bullets.remove(bullet)
        elif bullet.body.x > context.game_window.get_width():
            context.left_bullets.remove(bullet)

    for bullet in context.right_bullets:
        bullet.body.x -= BULLET_VEL
        if bullet.is_hitting(context.left_spaceship):
            pygame.event.post(pygame.event.Event(
                LEFT_HIT, damage=bullet.damage))
            context.right_bullets.remove(bullet)
        elif bullet.body.x < 0:
            context.right_bullets.remove(bullet)


def handle_keys(context: GameContext) -> None:
    """Handles the acctions to do from the current pressed keys.

    Args:
        context: GameContext object with the context variables of the game.
    """
    pressed_keys = pygame.key.get_pressed()

    handle_left_spaceship_movement(context, pressed_keys)
    handle_right_spaceship_movement(context, pressed_keys)
