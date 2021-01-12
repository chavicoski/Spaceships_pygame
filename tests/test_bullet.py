import unittest

from utils.config import YELLOW
from utils.classes.spaceship import Spaceship
from utils.classes.bullet import Bullet


class TestBullet(unittest.TestCase):
    """Tests for bullet class"""

    def setUp(self) -> None:
        """Prepares the variables for each test in this class."""
        self.shooter_pos = (200, 100)
        self.shooter = Spaceship(image_file="spaceship_yellow.png",
                                 side="left",
                                 init_pos=self.shooter_pos)
        self.bullet = Bullet(shooter=self.shooter, color=YELLOW)

    def test_is_hitting(self) -> None:
        """Tests the funtion to check if a bullet is hitting a spaceship"""
        target_pos = (800, 300)
        target_spaceship = Spaceship(image_file="spaceship_red.png",
                                     side="right",
                                     init_pos=target_pos)
        self.assertFalse(self.bullet.is_hitting(target_spaceship),
                         msg="The bullet shouldn't be hitting the spaceship.")
        # Move bullet to target and check
        self.bullet.body.x = target_pos[0]
        self.bullet.body.y = target_pos[1]
        self.assertTrue(self.bullet.is_hitting(target_spaceship),
                        msg="The bullet should be hitting the spaceship.")
