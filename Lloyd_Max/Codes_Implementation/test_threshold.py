import time

import matplotlib.pyplot as plt
from lloyd_max import *
from sklearn.metrics import mean_squared_error

N = 100000
print("N =", N)

mu = 0
sigma = 1
samples = np.random.normal(mu, sigma, N)

'''plt.hist(samples, N // 10, density=True)
plt.plot(samples, np.zeros([samples.size]), 'ko', markersize=10, linewidth=2)
plt.xlabel('X')
plt.ylabel('pₓ(x)')
plt.title("X distribution (N=" + str(N) + ")")
plt.show()'''

thresholds = np.arange(0, 0.3, 0.005)
thresholds = [0.2, 0.125, 0.1, 0.05, 0.01, 0.001]
t = []
distortions = []
for threshold in thresholds:
    print("threshold =", threshold)
    t1 = time.time()
    level_extremes = lloyd_max_algorithm(samples, threshold, levels_num=8)
    t.append(time.time()-t1)
    samples_quantized = quantize_samples(samples, level_extremes)
    distortion = mean_squared_error(samples, samples_quantized)
    distortions.append(distortion)
    print("Mean quadratic distortion:", distortion)

plt.figure()
plt.plot(thresholds, distortions, color='green')
plt.xlabel('threshold')
plt.ylabel('d(X,Q(X))')
plt.legend()
plt.title("Distortion varying threshold")
plt.show()

'''plt.figure()
plt.plot(thresholds, t, color='blue')
plt.xlabel('threshold')
plt.ylabel('time')
plt.legend()
plt.title("Quantization time varying threshold")
plt.show()'''