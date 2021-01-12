import numpy as np
import pygame
from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step

from utils.game_utils import update_window
from dqn.dqn_game_api import init_game, reset_game, perform_game_action, get_game_screenshot


OBSERVATION_FRAMES = 1  # Number of consecutive frames that forms an observation
TRANSITION_DISCOUNT = 1.0


class GameEnv(py_environment.PyEnvironment):

    def __init__(self):
        self.context = init_game()
        # 5 actions: move up, down, left, right and shoot
        """For observations of more than one screenshot
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(OBSERVATION_FRAMES,), dtype=np.int32, minimum=0, maximum=4, name="action")
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(OBSERVATION_FRAMES,  # The observation is made of several shots
                   self.context.game_window.get_width(),
                   self.context.game_window.get_height(),
                   3),  # 3 because is a RGB image
            dtype=(np.float32),
            minimum=0,
            maximum=1,
            name="game_screenshot")
        """
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=4, name="action")
        # The agents observe the screenshots of the game
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(self.context.game_window.get_width(),
                   self.context.game_window.get_height(),
                   3),  # Is a RGB image
            dtype=np.float32,
            minimum=0,
            maximum=1,
            name="game_screenshot")
        self._hp_state = [self.context.left_spaceship.health,
                          self.context.right_spaceship.health]
        self._episode_ended = False

    def observation_spec(self) -> array_spec.BoundedArraySpec:
        """Return observation_spec."""
        return self._observation_spec

    def action_spec(self) -> array_spec.BoundedArraySpec:
        """Return action_spec."""
        return self._action_spec

    def _reset(self) -> time_step.TimeStep:
        """Return initial_time_step."""
        self.context = reset_game(self.context)
        update_window(self.context)  # Refresh game screen
        self._hp_state = [self.context.left_spaceship.health,
                          self.context.right_spaceship.health]
        self._episode_ended = False

        """For observations of more than one screenshot
        game_frames = []
        for _ in range(0, OBSERVATION_FRAMES):
            game_frames.append(get_game_screenshot(self.context))
        """
        game_frames = get_game_screenshot(self.context)

        return time_step.restart(np.array(game_frames, dtype=np.float32))

    def _step(self, action: time_step.TimeStep) -> time_step.TimeStep:
        """Apply action and return new time_step."""
        if self._episode_ended:
            return self.reset

        """For observations of more than one screenshot
        game_frames = []
        for sub_action in action:
            perform_game_action(self.context, sub_action)
            game_frames.append(get_game_screenshot(self.context))
        """
        perform_game_action(self.context, action)
        game_frames = get_game_screenshot(self.context)

        # Compute reward
        reward = -1  # We penalize just moving
        if self.context.left_spaceship.is_dead():
            # We won the game
            self._episode_ended = True
            reward = 1000
        elif self.context.right_spaceship.is_dead():
            # We losed the game
            self._episode_ended = True
            reward = -1000
        else:
            if self.context.left_spaceship.health < self._hp_state[0]:
                # We hit the enemy spaceship
                reward += 50 * \
                    (self._hp_state[0] - self.context.left_spaceship.health)
            if self.context.right_spaceship.health < self._hp_state[1]:
                # We get hit by the enemy spaceship
                reward -= 50 * \
                    (self._hp_state[1] - self.context.right_spaceship.health)

        # Reset hp counters after damage computation
        self._hp_state = [self.context.left_spaceship.health,
                          self.context.right_spaceship.health]

        if self._episode_ended:
            return time_step.termination(
                np.array(game_frames, dtype=np.float32), reward=reward)
        else:
            return time_step.transition(
                np.array(game_frames, dtype=np.float32), reward=reward, discount=TRANSITION_DISCOUNT)
