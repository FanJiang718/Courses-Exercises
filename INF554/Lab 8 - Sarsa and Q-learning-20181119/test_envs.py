import gym
import numpy as np
env = gym.make('FrozenLake-v0')

Q = np.zeros([env.observation_space.n, env.action_space.n])
lr = 0.1
gamma = 0.99
num_episodes = 100000
num_iterations = 200
rewards = np.zeros(num_episodes)
epsilon = 0.01
SARSA = False
QLEARNING = True

if SARSA:
    rList = []
    for i in range(num_episodes):
        state = env.reset()
        rAll = 0
        done = False
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) * (1. / (i + 1)))
        while not done:
            new_state, reward, done, _ = env.step(action)
            if i % 500 == 0 and i is not 0:
                env.render()
                print(new_state)
            if np.random.rand() < epsilon:
                new_action = env.action_space.sample()
            else:
                new_action = np.argmax(Q[new_state, :]+ np.random.randn(1, env.action_space.n) * (1. / (i + 1)))

            Q[state, action] = Q[state, action] + lr * (reward + gamma * Q[new_state, new_action] - Q[state, action])
            rAll += reward
            state = new_state
            action = new_action
        rList.append(rAll)
        if i % 500 == 0 and i is not 0:
            print("Success rate: " + str(sum(r List) / i))

if QLEARNING:
    lr = 0.85
    gamma = 0.99
    rList_Q = []
    for i in range(num_episodes):
        state = env.reset()
        rAll = 0
        done = False
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) * (1. / (i + 1)))
        while not done:
            new_state, reward, done, _ = env.step(action)
            if i % 500 == 0 and i is not 0:
                env.render()
                print(new_state)
            Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])

            rAll += reward
            state = new_state
        rList_Q.append(rAll)
        if i % 500 == 0 and i is not 0:
            print("Success rate: " + str(sum(rList_Q) / i))




print("Success rate (SARSA): " + str(sum(rList)/num_episodes))

print("Success rate (Q-Learning): " + str(sum(rList_Q)/num_episodes))


"""
print("State space dimension is:", env.observation_space.shape)
print("State upper bounds:", env.observation_space.high)
print("State lower bounds:", env.observation_space.low)
print("Number of actions is:", env.action_space.n)


"""
