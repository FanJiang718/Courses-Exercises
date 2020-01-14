# used tutorial https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0
# author Akhan Ismailov
# Q-learning algorithm, line 24

import gym
import numpy as np

env = gym.make('FrozenLake-v0')
from gym import wrappers
env = wrappers.Monitor(env, '/tmp/FrozenLake-v0-experiment-15')

Q = np.zeros([env.observation_space.n, env.action_space.n])
lr = 0.85
gamma = 0.99
num_episodes = 2000
num_iterations = 200
rewards = np.zeros(num_episodes)

for episode in range(num_episodes):
    state = env.reset()
    for iteration in range(num_iterations):
        action = np.argmax( Q[state, :] + np.random.randn(1, env.action_space.n)*(1./(episode+1)) )
        state_new, reward, done, _ = env.step(action)
        Q[state, action] = Q[state, action] + lr*(reward + gamma*np.max(Q[state_new,:]) - Q[state, action])
        state = state_new

        if done or iteration == num_iterations-1:
            rewards[episode] = reward

        if done:
            break

def find_conseq_max():
    sum_cur = sum(rewards[0:100])
    maxx = sum_cur
    for i in range(100, num_episodes):
        sum_cur += rewards[i] - rewards[i-100]
        maxx = max(maxx, sum_cur)
    return maxx / 100

print find_conseq_max()