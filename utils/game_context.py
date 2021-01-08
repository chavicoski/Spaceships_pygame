from pygame import Surface, Rect


class GameContext:
    """Class to handle the global variables of the game."""

    def __init__(self,
                 game_window: Surface,
                 barrier: Rect,
                 yellow_spaceship: Surface,
                 red_spaceship: Surface,
                 yellow_rect: Rect,
                 red_rect: Rect):
        """Context constructor

        Args:
            game_window: Surface object of the game window.
            yellow_spaceship: Surface (image) of the yellow spaceship.
            red_spaceship: Surface (image) of the red spaceship.
            yellow_rect: Rect that represents the yellow spaceship.
            red_rect: Rect that represents the red spaceship.
        """
        self.game_window = game_window
        self.barrier = barrier
        self.yellow_spaceship = yellow_spaceship
        self.red_spaceship = red_spaceship
        self.yellow_rect = yellow_rect
        self.red_rect = red_rect
