import matplotlib.pyplot as plt
import numpy as np
import time

from lloyd_max import *
from sklearn.metrics import mean_squared_error



def bench_dist(samples, dist_info, ylim, xmi=-6, xma=6):
    t1 = time.time()
    level_extremes = lloyd_max_algorithm(samples, 0.000001, levels_num=8)
    print("Time:", time.time() - t1)
    samples_quantized = quantize_samples(samples, level_extremes)
    distortion = mean_squared_error(samples, samples_quantized)
    print("Mean quadratic distortion:", round(distortion,5))
    i = 0
    for level, extremes in level_extremes.items():
        ri = float(i) / float(8)
        gi = 1. - ri
        bi = 0.
        xmin = extremes[0] if extremes[0] != float('-inf') else min(samples) - 100
        xmax = extremes[1] if extremes[1] != float('inf') else max(samples) + 100
        plt.axvspan(xmin, xmax, alpha=0.35, color=(ri, gi, bi))
        ri = float(i) / float(8)
        gi = min([1. - ri, 0.8])
        plt.text(level-0.27, ylim - ylim/19, round(level,2), fontsize=6, color=(ri, gi, bi))
        plt.plot([level], [ylim], color=(ri, gi, bi), marker='D', linestyle='none')
        i += 1


    plt.hist(samples, N // 50, density=True, color="mediumblue", alpha=0.8)
    plt.plot(samples, np.zeros([samples.size]), 'ko', markersize=10, linewidth=2, alpha=0.5)
    plt.xlabel('X')
    plt.ylabel('f(x)')
    plt.xlim(xmi, xma)
    plt.title(dist_info)
    plt.show()


N = 100000
print("N =", N)



'''mu = 0
sigma = 1
samples = np.random.normal(mu, sigma, N)
print("mean =", mu, "- standard deviation =", sigma)
bench_dist(samples, "X normal distribution [mean=" + str(mu) + ", standard deviation=" + str(sigma) + "] (N=" + str(N) + ")", 0.6)

mu = 2
sigma = 1
samples = np.random.normal(mu, sigma, N)
print("mean =", mu, "- standard deviation =", sigma)
bench_dist(samples, "X gaussian distribution [mean=" + str(mu) + ", standard deviation=" + str(sigma) + "] (N=" + str(N) + ")", 0.6)

mu = 0
sigma = 1.5
samples = np.random.normal(mu, sigma, N)
print("mean =", mu, "- standard deviation =", sigma)
bench_dist(samples, "X gaussian distribution [mean=" + str(mu) + ", standard deviation=" + str(sigma) + "] (N=" + str(N) + ")", 0.3)'''

samples = np.random.uniform(-1, 1, N)
print("X uniform distribution")
bench_dist(samples, "X uniform distribution", 0.190)

'''scale=1
samples = np.random.exponential(scale, N)
print("exponential")
bench_dist(samples, "X exponential distribution [scale=" + str(scale)+ "]", 1.2, xmi=0, xma=12)'''
