import time

import matplotlib.pyplot as plt

from decoder import decode, recover_symbol_neighbours
from encoder import encode
import core
import math
import numpy as np

from lt_codes.distributions import robust_distribution


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

color_v = [["darkred", "red", "salmon", "lightsalmon"],
           ["midnightblue", "mediumblue", "royalblue", "cornflowerblue"],
           ["darkgreen", "green", "seagreen", "mediumseagreen"]]

block_size = 1024
input_size = 102400
blocks = core.generate_random_blocks(input_size=input_size, l=block_size)
n_blocks = len(blocks)
print("Blocks: {}".format(n_blocks))

delta_v = [0.4, 0.2, 0.1]
c_v = [[0.2, 0.1, 0.05, 0.035], [0.18, 0.07, 0.04, 0.017], [0.055, 0.043, 0.022, 0.015]]
p_K_eff_K_v = [[[] for _ in range(4)] for _ in delta_v]
N_TRIAL = 1000 #1000

for i_delta in range(len(delta_v)):
    delta = delta_v[i_delta]

    K = n_blocks + (np.log(n_blocks/delta))**2*np.sqrt(n_blocks)
    print("K =", K)

    for i_c in range(len(c_v[i_delta])):
        c = c_v[i_delta][i_c]

        robust_distribution(n_blocks, c, delta, draw_dist=True, color_dist=color_v[i_delta][i_c])
        #plt.savefig('dist_c' + str(c) + '_delta' + str(delta) + '.png')

        Keff_under_K = 0
        print("\n--------> c = ", c, "- delta =", delta)
        trial_i=0
        for trial_i in range(N_TRIAL):
            trial_i += 1
            core.seed_r = int(time.time_ns())
            # Split the file in blocks and compute how many symbols produce (according redundancy)
            print("\n----> Trial", trial_i)
            print("Input size: {}".format(convert_size(input_size)))

            symbols = []
            solved_blocks_count  = 0
            solved_blocks = [None] * n_blocks
            print("Simulation in progress...", flush=True)

            for curr_symbol in encode(blocks, c=c, delta=delta, debug=False):
                symbols.append(curr_symbol)

                curr_symbol = recover_symbol_neighbours(curr_symbol, n_blocks)

                solved_blocks, solved_blocks_count, symbols = decode(symbols, solved_blocks, solved_blocks_count, debug=False)

                if curr_symbol.index >= K or solved_blocks_count == n_blocks:
                    break

            if solved_blocks_count == n_blocks:
                print("File decoded correctly!")
                Keff_under_K += 1
            else:
                print("All blocks are not recovered!")

            p_K_eff_K = Keff_under_K / trial_i
            p_K_eff_K_v[i_delta][i_c].append(p_K_eff_K)
            print("Success Rate =", p_K_eff_K)

        print("\nRESULT: Success Rate (over "+str(N_TRIAL)+" trials) =", p_K_eff_K_v[i_delta][i_c][-1])

    plt.figure()
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(np.arange(N_TRIAL), p_K_eff_K_v[i_delta][0], color=color_v[i_delta][0], label="delta="+str(delta)+",c="+str(c_v[i_delta][0]))
    ax.plot(np.arange(N_TRIAL), p_K_eff_K_v[i_delta][1], color=color_v[i_delta][1], label="delta="+str(delta)+",c="+str(c_v[i_delta][1]))
    ax.plot(np.arange(N_TRIAL), p_K_eff_K_v[i_delta][2], color=color_v[i_delta][2], label="delta="+str(delta)+",c="+str(c_v[i_delta][2]))
    ax.plot(np.arange(N_TRIAL), p_K_eff_K_v[i_delta][3], color=color_v[i_delta][3], label="delta="+str(delta)+",c="+str(c_v[i_delta][3]))
    plt.title("Decoding Success Rate with K encoding symbols")
    ax.set_xlabel('trial')
    ax.set_ylabel('Mean Success Rate until current trial')
    ax.legend()

    plt.axhspan(0, 1-delta, facecolor='red', alpha=0.25)
    plt.ylim(0.4, 1)
    ax.legend()
    plt.show()

    fig.savefig('delta'+str(delta)+'.png')
