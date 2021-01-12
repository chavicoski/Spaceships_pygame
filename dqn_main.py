import pygame
from tf_agents.environments import tf_py_environment

from dqn.game_env import GameEnv
from dqn.models import ConvQNetwork


if __name__ == "__main__":
    # Create a TF agents environment from my py environment
    env = GameEnv()
    train_env = tf_py_environment.TFPyEnvironment(env)
    #eval_env = tf_py_environment.TFPyEnvironment(env)
