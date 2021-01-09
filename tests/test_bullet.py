import sys
sys.path.append(".")

import unittest

from utils.config import YELLOW
from utils.spaceship import Spaceship
from utils.bullet import Bullet


class TestBullet(unittest.TestCase):
    def setUp(self):
        self.shooter_pos = (200, 100)
        self.shooter = Spaceship(image_file="spaceship_yellow.png",
                                 side="left",
                                 init_pos=self.shooter_pos
                                 )
        self.bullet = Bullet(shooter=self.shooter, color=YELLOW)

    def test_is_hitting(self):
        """Tests the funtion to check is a bullet is hitting a spaceship"""
        target_pos = (800, 300)
        target_spaceship = Spaceship(image_file="spaceship_red.png",
                                     side="right",
                                     init_pos=target_pos
                                     )
        self.assertFalse(self.bullet.is_hitting(target_spaceship),
                         msg="The bullet shouldn't be hitting the spaceship.")
        # Move bullet to target and check
        self.bullet.body.x = target_pos[0]
        self.bullet.body.y = target_pos[1]
        self.assertTrue(self.bullet.is_hitting(target_spaceship),
                        msg="The bullet should be hitting the spaceship.")


if __name__ == "__main__":
    unittest.main()
