import pygame

from .spaceship import Spaceship


class Bullet:
    """Class that implements the bullets fired by the spaceships."""

    def __init__(self,
                 shooter: Spaceship,
                 color: tuple[int, int, int],
                 bullet_width: float = 10.0,
                 bullet_height: float = 5.0,
                 bullet_damage: int = 1):
        """Bullet constructor.

        Args:
            shooter: Spaceship object that fires the bullet
            color: RGB triplet with the color of the bullet.
            bullet_width: float with the width of the bullet projectile.
            bullet_height: float with the height of the bullet projectile.
            bullet_damage: The damage that the bullet does when hitting a spaceship.
        """
        self.color = color
        self.damage = bullet_damage
        x_pos, y_pos = shooter.body.x, shooter.body.y
        body_width, body_height = shooter.body.width, shooter.body.height
        if shooter.side == "left":
            self.body = pygame.Rect(
                x_pos + body_width, int(y_pos + body_height/2 - bullet_height/2), bullet_width, bullet_height)
        else:  # shooter.side must be "right"
            self.body = pygame.Rect(
                x_pos - bullet_width, int(y_pos + body_height/2 - bullet_height/2), bullet_width, bullet_height)

    def is_hitting(self, spaceship: Spaceship) -> bool:
        """Checks if the bullet is hitting the spaceship.

        Args:
            spaceship: The spaceship to check if we are hitting.

        Returns:
            A bool that says if the bullet is hitting the spaceship.
        """
        return bool(spaceship.body.colliderect(self.body))
