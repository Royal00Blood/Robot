import numpy as np
import gym
import random
from collections import deque

import matplotlib.pyplot as plt 
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# Buffer_Memory_ complit
class Memory:
    def __init__(self,max_size):
        self.buffer = deque(maxlen = max_size)

    def push(self, state, action, reward, next_state, done):
        experience = (state, action, np.array([reward]), next_state, done)
        self.buffer.append(experience)

    def sample(self, batch_size):
        state_batch = []
        action_batch = []
        reward_batch = []
        next_state_batch = []
        done_batch = []
    
        batch = random.sample(self.buffer,batch_size)

        for experience in batch:
            state, action, reward, next_state, done = experience
            state_batch.append(state)
            action_batch.append(action)
            reward_batch.append(reward)
            next_state_batch.append(next_state)
            done_batch.append(done)
        
        return state_batch, action_batch, reward_batch, next_state_batch, done_batch
    
    def __len__(self):
        return len(self.buffer)
####################################################################################################
class OUNoise(object):
    def __init__(self,action_space, mu = 0.0, theta = 0.15, max_sigma = 0.3, min_sigma = 0.3, decay_period = 100000):
        self.mu = mu
        self.theta = theta
        self.sigma = max_sigma
        self.max_sigma = max_sigma
        self.min_sigma = min_sigma
        self.dacay_period = decay_period
        self.action_dim = action_space.shape[0]
        self.low = action_space.low
        self.high = action_space.high
        self.reset()

    def reset(self):
        self.state = np.ones(self.action_dim) * self.mu

    def evolve_state(self):
        x = self.state
        dx = self.theta * (self.mu - x) + self.sigma * np.random.randn(self.action_dim)
        self.state = x + dx
        return self.state
    
    def get_action(self, action, t = 0):
        ou_state = self.evolve_state()
        self.sigma = self.max_sigma - (self.max_sigma - self.min_sigma) * min(1.0, t / self.dacay_period)
        return np.clip(action + ou_state, self.low, self.high)


class NormalizedEnv (): # gym.ActionWrapper
    def _action(self,action):
        act_k = (self.action_space.high - self.action_space.low)/2
        act_b = (self.action_space.high + self.action_space.low)/2
        return act_k * action + act_b
    
    def _reverse_action(self,action):
        act_k_inv = 2./(self.action_space.high - self.action_space.low)
        act_b = (self.action_space.high + self.action_space.low)/2
        return act_k_inv * (action-act_b)


import torch
import torch.nn as nn 
import torch.nn.functional as F
import torch.autograd
from torch.autograd import Variable

class Critic(nn.Module):

    def __init__(self,input_size,hidden_size,output_size):
        super(Critic,self).__init__()
        self.linear1 = nn.Linear(input_size,hidden_size)
        self.linear2 = nn.Linear(hidden_size,hidden_size)
        self.linear3 = nn.Linear(hidden_size,output_size)

    def forward(self, state, action):
        x = torch.cat([state,action], 1)
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = self.linear3(x)
        return x
 
class Actor(nn.Module):
    def __init__(self, input_size, hidden_size, output_size,learning_rate = 3e-4):
        super(Actor,self).__init__()
        self.linear1 = nn.Linear(input_size,hidden_size)
        self.linear2 = nn.Linear(hidden_size,hidden_size)
        self.linear3 = nn.Linear(hidden_size,output_size)

    def forward(self, state):
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = torch.tanh(self.linear3(x))
        return x


# def Env_take_info(new_state):
#     state = new_state
    
