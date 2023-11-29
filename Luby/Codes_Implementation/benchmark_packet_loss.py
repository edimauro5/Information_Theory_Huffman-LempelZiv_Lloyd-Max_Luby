import random
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

delta = 0.2
c = 0.017
packet_loss_prob_v = [0, 0.2, 0.4, 0.6]
p_K_eff_K_v = [[] for _ in packet_loss_prob_v] # err probs
N_TRIAL = 1000 #1000

robust_distribution(n_blocks, c, delta, draw_dist=True, color_dist='blue')

for packet_loss_prob_i in range(len(packet_loss_prob_v)):
    packet_loss_prob = packet_loss_prob_v[packet_loss_prob_i]

    K = n_blocks + (np.log(n_blocks/delta))**2*np.sqrt(n_blocks)
    print("K =", K)

    Keff_under_K = 0
    print("\n--------> c = ", c, "- delta =", delta, " - packet_loss_prob =", packet_loss_prob)
    trial_i=0
    for trial_i in range(N_TRIAL):
        trial_i += 1
        core.seed_r = int(time.time_ns())
        print(core.seed_r)
        # Split the file in blocks and compute how many symbols produce (according redundancy)
        print("\n----> Trial", trial_i)
        print("Input size: {}".format(convert_size(input_size)))

        symbols = []
        solved_blocks_count  = 0
        solved_blocks = [None] * n_blocks
        print("Simulation in progress...", flush=True)
        lost_packets_n = 0
        kk = 0

        packet_loss_seed = 42
        #random.seed(int(time.time_ns()))
        for curr_symbol in encode(blocks, c=c, delta=delta, debug=False):

            # packet loss with probability packet_loss_prob
            random.seed(packet_loss_seed)
            if random.random() < packet_loss_prob:
                lost_packets_n += 1
            else:
                kk += 1
                symbols.append(curr_symbol)
                curr_symbol = recover_symbol_neighbours(curr_symbol, n_blocks)
                solved_blocks, solved_blocks_count, symbols = decode(symbols, solved_blocks, solved_blocks_count, debug=False)

            # curr_symbol.index
            if kk >= K or solved_blocks_count == n_blocks:
                break

        if solved_blocks_count == n_blocks:
            print("File decoded correctly!")
            Keff_under_K += 1
        else:
            print("All blocks are not recovered!")

        p_K_eff_K = Keff_under_K / trial_i
        p_K_eff_K_v[packet_loss_prob_i].append(p_K_eff_K)
        print("Success Rate =", p_K_eff_K)
        print("Received packets =", kk)
        print("Number of packets lost =", lost_packets_n, "(" + str(round(lost_packets_n/curr_symbol.index*100, 3))+'%)')


    print("\nRESULT: Success Rate (over "+str(N_TRIAL)+" trials) =", p_K_eff_K_v[packet_loss_prob_i][-1])

plt.figure()
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(np.arange(N_TRIAL), np.array(p_K_eff_K_v[0]), color=color_v[0][0], label="delta="+str(delta)+",c="+str(c)+",packet_loss_prob="+str(packet_loss_prob_v[0]))
ax.plot(np.arange(N_TRIAL), np.array(p_K_eff_K_v[1]), color=color_v[0][1], label="delta="+str(delta)+",c="+str(c)+",packet_loss_prob="+str(packet_loss_prob_v[1]))
ax.plot(np.arange(N_TRIAL), np.array(p_K_eff_K_v[2]), color=color_v[0][2], label="delta="+str(delta)+",c="+str(c)+",packet_loss_prob="+str(packet_loss_prob_v[2]))
ax.plot(np.arange(N_TRIAL), np.array(p_K_eff_K_v[3]), color=color_v[0][3], label="delta="+str(delta)+",c="+str(c)+",packet_loss_prob="+str(packet_loss_prob_v[3]))

plt.title("Decoding Success Rate with K enc. symbols (effectively received)")
ax.set_xlabel('trial')
ax.set_ylabel('Mean Success Rate until current trial')
ax.legend()

#plt.axhspan(0, 1-delta, facecolor='grey', alpha=0.25)
#plt.ylim(0.3, 1)
ax.legend()
plt.show()

fig.savefig('err_delta'+str(delta)+'.png')
