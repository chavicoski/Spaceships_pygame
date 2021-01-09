import sys
sys.path.append(".")
import unittest

from utils.spaceship import Spaceship


class TestSpaceship(unittest.TestCase):
    def setUp(self):
        self.name = "TestSpaceship"
        self.init_pos = (700, 250)
        self.spaceship = Spaceship(image_file="spaceship_red.png",
                                   side="right",
                                   init_pos=self.init_pos,
                                   name=self.name)

    def test_constructor_coordinates(self):
        """Tests if the initial position set by the constructor correct."""
        self.assertEqual(self.init_pos[0], self.spaceship.body.x,
                         msg="The x coordinate is not correct.")
        self.assertEqual(self.init_pos[1], self.spaceship.body.y,
                         msg="The y coordinate is not correct.")

    def test_constructor_name(self):
        """Tests if the constructor sets correctly the name in the case that it is provided or not"""
        # Check the spaceship with the name provided in the constructor
        self.assertEqual(self.name, self.spaceship.name,
                         msg=f"The name should be \"{self.name}\" but is \"{self.spaceship.name}\"")

        # Check the spaceship without the name provided in the constructor
        no_name_spaceship = Spaceship(image_file="spaceship_red.png",
                                      side="right",
                                      init_pos=self.init_pos)
        self.assertEqual("right_spaceship", no_name_spaceship.name,
                         msg=f"The name should be \"right_spaceship\" but is \"{no_name_spaceship.name}\"")

    def test_is_dead(self):
        """Tests the dead checker function of the spacechip."""
        self.spaceship.health = 1
        self.assertFalse(self.spaceship.is_dead(),
                         msg="Spaceship shouldn't be dead with more than 0 health.")
        self.spaceship.health = 0
        self.assertTrue(self.spaceship.is_dead(),
                        msg="Spaceship should be dead with 0 health.")
        self.spaceship.health = -2
        self.assertTrue(self.spaceship.is_dead(),
                        msg="Spaceship should be dead with negative health.")


if __name__ == "__main__":
    unittest.main()
