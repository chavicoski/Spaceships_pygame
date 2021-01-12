from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten
import tf_agents


class ConvQNetwork(tf_agents.networks.Network):
    def __init__(self, n_actions):
        self._forward = Sequential([
            Conv2D(64, (3, 3), activation="relu"),
            Conv2D(64, (3, 3), activation="relu"),
            Flatten(),
            Dense(512),
            Dense(n_actions)
        ])

    def call(self, observations, state=()):
        logits = self._forward(observations)
        return logits, state
