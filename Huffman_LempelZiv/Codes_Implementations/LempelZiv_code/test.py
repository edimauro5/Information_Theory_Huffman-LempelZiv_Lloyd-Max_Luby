from LZ import *
from bitstring import BitArray
import time
from LZ_extra import *
import numpy as np

if __name__ == '__main__':
    lorem = [1, 2, 5, 10, 30, 100, 300, 500, 700, 999]
    
    #for i in range(len(lorem)):
        #print("\nLZ algorithm with lorem"+str(lorem[i])+".txt")
        #data = '0010111010010111011011'
    #file = open("../Huffman_code/data/data.txt", "rb")
    file = open("new.txt", "rb")
    #pmf1 = {'A':0.25, 'B':0.25, 'C':0.25, 'D':0.25}
    #data = ''.join(list(np.random.choice(list(pmf1.keys()), 100000, p = list(pmf1.values()))))

    #data = file.read()
    #data = BitArray(data.encode()).bin
    data = BitArray(file.read()).bin
    #print(data)
    t1 = time.time()
    outputEnc, lenEnd = lzEncode(data)
    t2 = time.time()
    #print(outputEnc)
    print("Encoding time:", t2-t1)
    #print(len(data))
    #print(len(outputEnc))
    print('Encoded input:', len(outputEnc))
    '''t1 = time.time()
    outputDec = lzDecode(outputEnc, lenEnd)
    t2 = time.time()
    print("Decoding time:", t2-t1)
    print('Original input:', len(outputDec))'''
    
    compareSpaceUsage(data, outputEnc)
        
        
        
    