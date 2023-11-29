from Codes_Implementations.Huffman_code.Huffman import *
from Codes_Implementations.Huffman_code.Huffman_extra import compareSpaceUsage as huffComp
from Codes_Implementations.Huffman_code.Huffman_extra import *
import numpy as np
import time
from itertools import *
from math import log
from fractions import Fraction
import matplotlib.pyplot as plt
from scipy.stats import entropy
from Codes_Implementations.LempelZiv_code.LZ import *
from bitstring import BitArray
from Codes_Implementations.LempelZiv_code.LZ_extra import *
from Codes_Implementations.LempelZiv_code.LZ_extra import compareSpaceUsage as LZComp



'''numChar = [932, 1377, 4210, 7546, 21917, 75889, 227833, 383458, 521852, 751679]
huffCompr = [47.21, 47.25, 47.02, 47.008, 47.036, 47.005, 46.97, 46.95, 46.98, 46.96]
LZCompr = [-11.17, -7.42, 0.93, 6.58, 14.17, 23.78, 31.98, 36.72, 39.53, 42.81]
huffEncTime = [0.001, 0.001, 0.001, 0.0035, 0.01, 0.0346, 0.09, 0.19, 0.37, 0.63]
LZEncTime = [0.003, 0.006, 0.018, 0.03, 0.07, 0.22, 0.72, 1.35, 1.97, 3.12]
huffDecTime = [0.001, 0.001, 0.0025, 0.006, 0.02, 0.0711, 0.177, 0.35, 0.57, 0.93]
LZDecTime = [0.001, 0.003, 0.005, 0.01, 0.04, 0.1, 0.34, 0.69, 1.08, 2.05]

plotCompression(numChar, huffCompr, LZCompr)
plotEncTime(numChar, huffEncTime, LZEncTime)
plotDecTime(numChar, huffDecTime, LZDecTime)'''


'''n = []
entropies = []
entropies1 = []
entr = 0
lengths = []
compressions = []
sizes = []
pmf1 = {'A':0.25, 'B':0.25, 'C':0.25, 'D':0.25}
pmf2 = {'A':0.3, 'B':0.35, 'C':0.35, 'D':0}
pmf3 = {'A':0.25, 'B':0.25, 'C':0.25, 'D':0.25}
pmf4 = {'A':0.25, 'B':0.2, 'C':0.1, 'D':0.09, 'E': 0.2, 'F': 0.16}
t = 1
for i in range(t):
    size = pow(10, i)
    
    data = list(np.random.choice(list(pmf4.keys()), 1000000, p = list(pmf4.values())))
#print("data", data)

    print("Comparison between the algorithm performance using true pmf and using false pmfs\n")
    print("Encoding and Decoding with given pmf1")
    outputEnc, huffmanTree, symCode, symFreq = huffmanEncode(data=data)
    huffmanDecode(outputEnc, huffmanTree)
    #print("Decoded output:", huffmanDecode(outputEnc, huffmanTree))
    compression = compareSpaceUsage(data, symCode)
    entr, length = compareLengthEntropy(symCode, data=data)
    entropies.append(entr)
    sizes.append(pow(10, i))
    compressions.append(compression)
    print("\n")
    for symbol in list(symFreq.keys()):
        print(symFreq[symbol] / len(data))
#pltEntrCompr(sizes, entropies, compressions)
print("\n")'''
huffCompr = []
LZCompr = []
tEncHuff = []
tDecHuff = []
tEncLZ = []
tDecLZ = []
numChar = [932, 1377, 4210, 7546, 21917, 75889, 227833, 383458, 521852, 751679]
lorem = [1, 2, 5, 10, 30, 100, 300, 500, 700, 999]
#pmf4 = {'A':0.25, 'B':0.2, 'C':0.1, 'D':0.09, 'E': 0.2, 'F': 0.16}
pmf4 = {'A':0.3, 'B':0.35, 'C':0.35, 'D':0}
pmf = pmf4
n = []
inputSize = [1, 2, 5, 8, 22, 75, 223, 375, 510, 735]
source_size = [800, 2000, 20000, 50000, 100000, 300000, 500000, 800000, 1000000]
source_size_kb = [800//1000, 2000//1000, 20000//1000, 50000//1000, 100000//1000, 300000//1000, 500000//1000, 800000//1000, 1000000//1000]

#for i in range(len(lorem)):


for x in range(len(source_size)):
    data = []
    data = list(np.random.choice(list(pmf.keys()), source_size[x], p = list(pmf.values())))
    with open("new.txt", "w") as f:
        for item in data:
            f.write("%s" % item)
    #print("\nHuffman algorithm with lorem"+str(lorem[(i)])+".txt")
    print("\nHuffman algorithm with x = " + str(x))
    #file = open("Codes_Implementations/files/lorem/lorem"+str(lorem[(i)])+".txt", "rb")
    
    #data = list(np.random.choice(list(pmf.keys()), 10000, p = list(pmf.values())))
    #print("data", data)
    
    '''data = []
    file = open("new.txt", "r")    
    while bytes := file.read(1):
        data.append(bytes)
    #print(data)
    #print("pmf bytes", pmf)
    t1 = time.time()
    outputEnc, huffmanTree, symCode = huffmanEncode(data=data, pmf=pmf)
    t2 = time.time()
    print("Encoding time:", t2 - t1)
    tEncHuff.append(t2-t1)
    #print(symCode)
    #print("Encoded output:", outputEnc)
    
    
    
    t1 = time.time()
    huffmanDecode(outputEnc, huffmanTree)
    t2 = time.time()
    print("Decoding time:", t2 - t1)
    #print("Decoded Output:", huffmanDecode(outputEnc, huffmanTree))
    tDecHuff.append(t2-t1)
    hCompr = huffComp(data, symCode)
    huffCompr.append(hCompr)
    #print("symCode:", symCode)
    entropy, length = compareLengthEntropy(symCode, data=data, pmf=pmf)
    n.append(x)'''
    
    #print("\nLZ algorithm with lorem"+str(lorem[i])+".txt")
    #data = '0010111010010111011011'
    #file = file = open("files/lorem/lorem"+str(lorem[(i)])+".txt", "rb")
    
    #print("\nLZ algorithm with lorem"+str(lorem[(i)])+".txt")

    #file = open("Codes_Implementations/files/lorem/lorem"+str(lorem[(i)])+".txt", "rb")
    data = []
    file = open("new.txt", "rb")  
    data = BitArray(file.read()).bin
    #data = file.read()
    
    t1 = time.time()
    outputEnc, lenEnd = lzEncode(data)
    t2 = time.time()
    tEncLZ.append(t2-t1)
    print("Encoding time:", t2-t1)
    print(len(data))
    print('Encoded input:', len(outputEnc))
    t1 = time.time()
    outputDec = lzDecode(outputEnc, lenEnd)
    t2 = time.time()
    print("Decoding time:", t2-t1)
    tDecLZ.append(t2-t1)
    print('Original input:', len(outputDec))
    
    LCompr = LZComp(data, outputEnc)
    LZCompr.append(LCompr)
    
    '''pmf_new = {}
    for symbol in list(pmf.keys()):
        #symString = symbol.decode()
        symString = symbol
        for s in list(pmf4.keys()):
            #sString = s.decode()
            sString = s
            symbolNew = symString + sString
            pmf_new[symbolNew] = pmf[symbol] * pmf4[s]
    #print("pmf_new", pmf_new)
            
    pmf = pmf_new'''
    #n.append(x)
    
plotCompression(source_size_kb, huffCompr, LZCompr)
#plotCompressionHuff(n, huffCompr)
#plotEncTime(inputSize, tEncHuff, tEncLZ)
#plotDecTime(inputSize, tDecHuff, tDecLZ)