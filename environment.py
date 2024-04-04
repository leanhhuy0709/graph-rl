'''environment.py: File này chứa lớp Environment, bao gồm 
việc khởi tạo môi trường, thực hiện hành động và lấy trạng thái 
tiếp theo và phần thưởng.
'''

import gym
from gym import spaces

# import const from utils/constant.py
from utils2.config import N_DISCRETE_ACTIONS, N_OBSERVATIONS


class Environment(gym.Env):
    def __init__(self):
        super(Environment, self).__init__()

        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions, Box for continuous
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        self.observation_space = spaces.Box(
            low=-10, high=10, shape=(N_OBSERVATIONS,))

    def step(self, action):
        # Execute one time step within the environment
        # Must return observation, reward, done, info
        pass

    def reset(self):
        # Reset the state of the environment to an initial state
        pass

    def render(self, mode='human'):
        # Render the environment to the screen (optional)
        pass
