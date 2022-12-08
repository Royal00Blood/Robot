import tensorflow as tf
from tensorflow.python.keras.layers import Input,Dense
import numpy as np 
import matplotlib.pyplot as plt 
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

def Env_take_info():
    state = 1##############
    action = 1###########
    reward = 2##################
    return state, action, reward
