import matplotlib.pyplot as plt
import numpy as np


def compute_initial_levels(samples, levels_num):
    min_sample = min(samples)
    max_sample = max(samples)
    region = (max_sample - min_sample) / levels_num
    levels = [min_sample+region/2 + i*region for i in range(levels_num)]
    return levels


def compute_extremes(samples, levels):
    extremes = np.zeros(len(levels)-1)
    # compute exact partition extremes
    for i in range(len(extremes)):
        extremes[i] = (levels[i] + levels[i+1])/2
    # compute partition extreme indexes
    extremes_indexes = np.zeros(len(levels)-1, 'int')
    j = 0
    for i in range(len(samples)):
        if j == len(extremes_indexes):
            break
        if samples[i] >= extremes[j]:
            extremes_indexes[j] = i
            j += 1
    return extremes_indexes


def compute_levels(samples, extremes):
    levels = np.zeros(len(extremes) + 1)
    for i in range(len(levels)):
        if i == 0:
            levels[i] = np.mean(samples[:extremes[i]])
        elif i == len(extremes):
            levels[i] = np.mean(samples[extremes[i-1]:])
        else:
            levels[i] = np.mean(samples[extremes[i-1]:extremes[i]])
    return levels


def get_level_extremes(levels, extremes):
    dict = {}
    for i in range(len(levels)):
        if i == 0:
            dict[levels[i]] = (float('-inf'), extremes[i])
        elif i == len(extremes):
            dict[levels[i]] = (extremes[i-1], float('inf'))
        else:
            dict[levels[i]] = (extremes[i-1], extremes[i])
    return dict


def lloyd_max_algorithm(samples, threshold, levels_num=8):
    samples = sorted(samples)
    diff = threshold + 1 #difference between levels and new_levels
    levels = compute_initial_levels(samples, levels_num)
    extremes = []
    iter_num = 0
    while diff > threshold:        
        extremes = compute_extremes(samples, levels)
        new_levels = compute_levels(samples, extremes)
        #diff = max(np.abs(new_levels-levels))
        diff = np.linalg.norm((new_levels - levels), ord=1)
        levels = new_levels
        iter_num += 1
    extremes = [samples[e] for e in extremes]
    level_extremes = get_level_extremes(levels, extremes)
    #print("Number of iterations:", iter_num)
    return level_extremes
    
           
def quantize_samples(samples, level_extremes):
    samples_quantized = []
    for x in samples:
        for level in level_extremes.keys():
            extremes = level_extremes[level]
            if extremes[0] <= x < extremes[1]:
                samples_quantized.append(level)
    return samples_quantized
    
    
