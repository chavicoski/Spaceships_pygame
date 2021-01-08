import pygame

from utils.game_api import setup_game, game_loop


def main():
    context = setup_game()
    game_loop(context)
    pygame.quit()


if __name__ == "__main__":
    main()
