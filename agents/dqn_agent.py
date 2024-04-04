'''dqn_agent.py: File này chứa lớp DQNAgent, bao gồm việc xây dựng mô hình, 
lựa chọn hành động, lưu trữ kinh nghiệm và huấn luyện mô hình.
'''

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

from utils2.config import GAMMA, EPSILON, EPSILON_MIN, EPSILON_DECAY, LEARNING_RATE, BATCH_SIZE, MODEL_PATH


class DQNAgent:
    def __init__(self, state_size: int, action_size: int):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = GAMMA
        self.epsilon = EPSILON
        self.epsilon_min = EPSILON_MIN
        self.epsilon_decay = EPSILON_DECAY
        self.learning_rate = LEARNING_RATE
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size,
                  activation=keras.activations.relu))
        model.add(Dense(24, activation=keras.activations.relu))
        model.add(Dense(self.action_size, activation=keras.activations.linear))
        model.compile(loss=keras.losses.mean_squared_error,
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        # Implement this
        pass

    def act(self, state):
        # Implement this
        pass

    def replay(self, batch_size):
        # Implement this
        pass

    def update_epsilon(self):
        # Implement this
        pass

    def load(self, name):
        # Implement this
        pass

    def save(self, name):
        # Implement this
        pass
