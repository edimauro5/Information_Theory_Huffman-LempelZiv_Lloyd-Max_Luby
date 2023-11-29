import os
import random
import time

import keyboard as keyboard

from decoder import decode, recover_symbol_neighbours
from encoder import encode
import core

#########################################################
# HOW TO RUN?
# run from terminal, in mpsa folder
# 2 sudo python3 lt_codes/simulation.py

filename = "lt_codes/files/example_json.txt"
filename_decoded = "lt_codes/files/example_json_decoded.txt"

packet_loss_prob = 0.6

with open(filename, "rb") as file:

    filesize = os.path.getsize(filename)
    print("Filesize: {} bytes".format(filesize))

    # Split the file in blocks and compute how many symbols produce (according redundancy)
    blocks = core.blocks_read(file, filesize)
    n_blocks = len(blocks)
    redundancy_max = 100000
    n_symbols_max = int(n_blocks * redundancy_max)

    print("Blocks: {}".format(n_blocks))

    symbols = []
    solved_blocks_count  = 0
    solved_blocks = [None] * n_blocks
    K = 0

    core.seed_r = int(time.time_ns())
    print(core.seed_r)

    packet_loss_seed = 45
    random.seed(packet_loss_seed)

    for curr_symbol in encode(blocks):

        #print(random.random())
        if random.random() < packet_loss_prob and K > 5:
            print("[PK_LOSS] Symbol", K, "lost!")
        # Simulating the loss of packets when pressing q
        #if keyboard.is_pressed('q'):  # if key 'q' is pressed
        #    print("[PK_LOSS] Symbol", K, "lost!")
        else:
            symbols.append(curr_symbol)
            curr_symbol = recover_symbol_neighbours(curr_symbol, n_blocks)

        solved_blocks, solved_blocks_count, symbols = decode(symbols, solved_blocks, solved_blocks_count)
        K += 1

        # slow down the simulation
        time.sleep(0.05)

        if curr_symbol.index > n_symbols_max or solved_blocks_count == n_blocks:
            break

    # recovered_blocks, recovered_n = decode(symbols, blocks_quantity=n_blocks)
    if solved_blocks_count != n_blocks:
        print("\nAll blocks are not recovered!")
        exit()
    else:
        print("\nFile decoded correctly!")

    print("K =", K)

    # Write down the recovered blocks in a copy
    with open(filename_decoded, "wb") as file_decoded:
        core.blocks_write(solved_blocks, file_decoded)
    print("Wrote {} bytes in {}".format(os.path.getsize(filename_decoded), filename_decoded), "\n")
