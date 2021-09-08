import environment_2d
import processing
import numpy as np
np.random.seed(4)
env = environment_2d.Environment(10, 6, 2)
processing.robo(env,random=True)