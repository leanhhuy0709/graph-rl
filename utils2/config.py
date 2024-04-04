
N_DISCRETE_ACTIONS = 4      # Number of discrete actions
N_OBSERVATIONS = 10         # Number of observations

GAMMA = 0.95                # Discount factor for future rewards

EPSILON = 1.0               # Initial exploration rate
EPSILON_MIN = 0.01          # Minimum exploration rate
EPSILON_DECAY = 0.995       # Decay rate for exploration

LEARNING_RATE = 0.001       # Learning rate for the DQN
BATCH_SIZE = 32             # Batch size for DQN
TRAINING_EPISODES = 1000    # Number of episodes for training
MODEL_PATH = "model.h5"     # Path to save the model
