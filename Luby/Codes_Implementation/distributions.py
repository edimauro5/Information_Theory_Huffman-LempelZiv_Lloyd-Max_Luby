import numpy as np

from core import *
import math
import matplotlib.pyplot as plt

def ideal_distribution(k):
    """ Create the ideal soliton distribution. 
    In practice, this distribution gives not the best results
    Cf. https://en.wikipedia.org/wiki/Soliton_distribution
    """

    probabilities = [0, 1 / k]      # p0, p1
    probabilities += [1 / (i * (i - 1)) for i in range(2, k+1)]

    return probabilities

def robust_distribution(k, c, delta, draw_dist=False, color_dist="navy"):
    """ Create the robust soliton distribution. 
    This fixes the problems of the ideal distribution
    Cf. https://en.wikipedia.org/wiki/Soliton_distribution
    """

    p = ideal_distribution(k)

    # The choice of M is not a part of the distribution ; it may be improved
    # We take the median and add +1 to avoid possible division by zero 

    if c is None:
        x = k // 2 + 1 # x must be integer
        R = k / x
        # WHY?
        # R = c*ln(k/ROBUST_FAILURE_PROBABILITY)*sqrt(k)
        # R = k / (k//2+1)
        # c*ln(k/ROBUST_FAILURE_PROBABILITY)*sqrt(k) = k / (k//2+1)
        # c = k  / [ (k//2+1) * ln(k/ROBUST_FAILURE_PROBABILITY)*sqrt(k) ]
    else:
        R = c * np.log(k / delta) * np.sqrt(k)
        x = int(k // R)  # make sure it is a integer

    tau = [0] + [1 / (i * x) for i in range(1, x)]
    tau += [math.log(R / delta) / x]
    tau += [0 for _ in range(x + 1, k + 1)]

    mu = np.add(tau, p)
    mu /= np.sum(mu)

    if draw_dist:
        kk = np.arange(0, k+1)
        fig = plt.figure(figsize=(8, 4))
        # creating the bar plot
        plt.bar(kk[:100], mu[:100], color=color_dist)
        plt.xlabel("Block index")
        plt.ylabel("mu(x)")
        plt.title("Robust Soliton Distribution [c="+str(c)+", delta="+str(delta)+"]")
        plt.show()

    return mu
