#!/usr/bin/env python

import math
import random
import matplotlib.pyplot as plt

def sample_beta(alpha, beta):
    x = math.log( random.random() )
    y = math.log( random.random() )
    
    return x / (x + y*alpha/beta)

bins = [0.01 * i for i in range(102)]
plt.hist([sample_beta(0.00001, 0.1) for k in range(10000000)], bins)
plt.show()

