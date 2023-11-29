from random import choices
from distributions import *

def get_degree_from(p_dist):
    """ Returns the random degree from a given distribution of probabilities.
    The degrees distribution must look like a Poisson distribution and the 
    degree of the first drop is 1 to ensure the start of decoding.
    """
    block_indexes = list(range(0, len(p_dist)))
    return choices(block_indexes, p_dist, k=1)[0]
   
def encode(blocks, c=None, delta=DELTA, debug=True):
    """ Iterative encoding - Encodes new symbols and yield them.
    Encoding one symbol is described as follows:

    1.  Randomly choose a degree according to the degree distribution, save it into "deg"
        Note: below we prefer to randomly choose all the degrees at once for our symbols.

    2.  Choose uniformly at random 'deg' distinct input blocs. 
        These blocs are also called "neighbors" in graph theory.
    
    3.  Compute the output symbol as the combination of the neighbors.
        In other means, we XOR the chosen blocs to produce the symbol.
    """
    blocks_n = len(blocks)
    p_dist = robust_distribution(blocks_n, c, delta)

    i = 0
    while True:
        # Generate random index associated to random degree, seeded with the symbol id
        d = get_degree_from(p_dist)
        # Get the random selection
        selection_indexes, d = generate_indexes(i, d, blocks_n)
        # Xor each selected array within each other
        symbol_data = blocks[selection_indexes[0]]
        for n in range(1, d):
            symbol_data = np.bitwise_xor(symbol_data, blocks[selection_indexes[n]])
        # Create symbol, then log the process
        symbol = Symbol(index=i, degree=d, data=symbol_data)
        if debug:
            print("[ENCODER] Released symbol", i)
        i += 1

        yield symbol

