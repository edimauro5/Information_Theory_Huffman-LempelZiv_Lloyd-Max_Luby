import time
import matplotlib.pyplot as plt
import matplotlib.scale as plt_scale
from decoder import decode, recover_symbol_neighbours
from encoder import encode
# from core import *
import core
import math


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


redundancy_max = 10000

input_size = 500000

l_size = [1024, 2048, 4096, 8192, 16384, 32768, 65536]

exe_time = []
code_rate = []

print("Input size: {}".format(convert_size(input_size)))

for l in l_size:
    print("\n")

    core.seed_r = int(time.time_ns())

    # Split the file in blocks and compute how many symbols produce (according redundancy)
    start_time = time.time()

    blocks = core.generate_random_blocks(input_size=input_size, l=l)

    n_blocks = len(blocks)
    n_symbols_max = int(n_blocks * redundancy_max)

    print("Blocks: {}".format(n_blocks))
    print("Simulation in progress...", flush=True)

    symbols = []
    solved_blocks_count = 0
    solved_blocks = [None] * n_blocks

    K = 0
    for curr_symbol in encode(blocks, c=0.5, delta=0.1, debug=False):

        curr_symbol = recover_symbol_neighbours(curr_symbol, n_blocks)

        symbols.append(curr_symbol)

        solved_blocks, solved_blocks_count, symbols = decode(symbols, solved_blocks, solved_blocks_count, debug=False)
        K += 1
        if curr_symbol.index > n_symbols_max or solved_blocks_count == n_blocks:
            break

    if solved_blocks_count != n_blocks:
        print("All blocks are not recovered!")
        exit()
    else:
        print("File decoded correctly!")

    end_time = time.time() - start_time
    rate = n_blocks/K

    exe_time.append(end_time)
    code_rate.append(rate)

    print("Execution time: %.4f" % end_time, "seconds")


plt.plot(l_size, exe_time, 'b', marker='o')
plt.title("Execution Time varying block size l")
plt.xlabel("l")
plt.xscale("log")
plt.xlabel(l_size)
plt.ylabel("Execution Time (s)")
plt.show()


