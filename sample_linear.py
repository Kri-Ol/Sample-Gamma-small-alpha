#!/usr/bin/env python

import math
import random
import matplotlib.pyplot as plt

# sample from linear distribution and plot it
bins = [0.1 * i for i in range(12)]
plt.hist([(1.0 - math.sqrt(random.random())) for k in range(10000)], bins)
plt.show()

