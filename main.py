'''main.py: File này chứa vòng lặp chính để huấn luyện và kiểm tra agent.
'''
import numpy as np

from agents.dqn_agent import DQNAgent
from environment import Environment
from utils2.config import TRAINING_EPISODES, BATCH_SIZE, MODEL_PATH


def main():
    # Initialize environment and agent
    env = Environment()
    agent = DQNAgent(env.state_size, env.action_size)

    for e in range(TRAINING_EPISODES):
        # Reset state at the start of each game
        state = env.reset()
        state = np.reshape(state, [1, env.state_size])

        done = False
        while not done:
            # Agent takes action
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, env.state_size])

            # Remember the previous state, action, reward, and done
            agent.remember(state, action, reward, next_state, done)

            # make next_state the new current state for the next frame.
            state = next_state

            # done becomes True when the game ends
            if done:
                # print the score and break out of the loop
                print("episode: {}/{}, score: {}"
                      .format(e, TRAINING_EPISODES, 69))
                break

        # train the agent with the experience of the episode
        agent.replay(BATCH_SIZE)

    # Save the weights
    agent.save(MODEL_PATH)


if __name__ == "__main__":
    main()
