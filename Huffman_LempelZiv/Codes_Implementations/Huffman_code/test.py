from Huffman import *
from Huffman_extra import *
import numpy as np
import time
from itertools import *

if __name__ == "__main__":
    n = []
    entropies = []
    entropiesEst = []
    entropies1 = []
    entr = 0
    lengths = []
    compressions = []
    sizes = []
    '''pmf1 = {'A':0.25, 'B':0.25, 'C':0.25, 'D':0.25}
    pmf2 = {'A':0.3, 'B':0.35, 'C':0.35, 'D':0}
    pmf3 = {'A':0.25, 'B':0.25, 'C':0.25, 'D':0.25}'''
    #pmf1 = {'A': 0.3, 'B': 0.3, 'C': 0.4, 'D': 0}
    pmf1 = {'A':0.25, 'B':0.25, 'C':0.25, 'D':0.25}
    pmf2 = {'A': 0.3, 'B': 0.35, 'C': 0.35, 'D': 0}
    pmf3 = {'A': 0.25, 'B': 0.25, 'C': 0.20, 'D': 0.3}
    t = 1
    #for i in range(1):
    #size = pow(10, i)
    
    data = list(np.random.choice(list(pmf1.keys()), 100000, p = list(pmf1.values())))
    #print("data", data)
    
    with open("data/data.txt", "w") as f:
        for item in data:
            f.write("%s" % item)
    data = []
    file = open("data/data.txt", "r")
    while bytes := file.read(1):
        data.append(bytes)
    #print("Comparison between the algorithm performance using true pmf and using false pmfs\n")
    print("Encoding and Decoding with PMF₁\n")
    t1 = time.time()
    outputEnc, huffmanTree, symCode = huffmanEncode(data=data, pmf=pmf1)
    t2 = time.time()
    print("Encoding time:", t2 - t1)
    t1 = time.time()
    huffmanDecode(outputEnc, huffmanTree)
    t2 = time.time()
    print("Decoding time:", t2 - t1)

    #print("Decoded output:", huffmanDecode(outputEnc, huffmanTree))
    compression = compareSpaceUsage(data, symCode)
    entr, length = compareLengthEntropy(symCode, data=data, pmf=pmf1)
    entropies.append(entr)
    #sizes.append(pow(10, i))
    compressions.append(compression)
    
    #print("\n")
    #pltEntrCompr(sizes, entropies, compressions)
    '''print("Encoding and Decoding with estimated pmf")
    outputEnc, huffmanTree, symCode = huffmanEncode(data)
    huffmanDecode(outputEnc, huffmanTree)
    #print("Decoded output:", huffmanDecode(outputEnc, huffmanTree))
    compareSpaceUsage(data, symCode)
    entr, length = compareLengthEntropy(data, symCode)
    
    symFreq = calculateFrequencies(data)
    est_pmf = {}
    for symbol in list(symFreq.keys()):
        est_pmf[symbol] = symFreq[symbol] / len(data)
    print(est_pmf)
    for symbol in list(pmf1.keys()):
        if symbol not in list(est_pmf.keys()):
            est_pmf[symbol] = 0
    print(est_pmf)
    divergence = entropy(list(pmf1.values()), list(est_pmf.values()))    
    print("divergence of pmf1 from estimated pmf:", divergence)
    print("\n")'''
    
    '''print("Encoding and Decoding with PMF₂")
    divergence = entropy(list(pmf1.values()), list(pmf2.values()), base=2)
    print("D(PMF₁||PMF2₂):", divergence)
    print("\n")
    outputEnc, huffmanTree, symCode = huffmanEncode(data=data, pmf=pmf2)
    huffmanDecode(outputEnc, huffmanTree)
    #print("Decoded output:", huffmanDecode(outputEnc, huffmanTree))
    compareSpaceUsage(data, symCode)
    entr, length = compareLengthEntropy(symCode, data=data, pmf=pmf2)
    

    
    print("\n")
    
    print("Encoding and Decoding with PMF₃")
    divergence = entropy(list(pmf1.values()), list(pmf3.values()), base=2)
    print("D(PMF₁||PMF₃):", divergence)
    outputEnc, huffmanTree, symCode = huffmanEncode(data=data, pmf=pmf3)
    print("\n")
    huffmanDecode(outputEnc, huffmanTree)
    #print("Decoded output:", huffmanDecode(outputEnc, huffmanTree))
    compareSpaceUsage(data, symCode)
    entr, length = compareLengthEntropy(symCode, data=data, pmf=pmf3)
    
    
    print("\n")'''
        
    
    
    '''print("Encoding and Decoding with given pmf")
    outputEnc, huffmanTree, symCode = huffmanEncode(data, pmf)
    huffmanDecode(outputEnc, huffmanTree)
    #print("Decoded output:", huffmanDecode(outputEnc, huffmanTree))
    compareSpaceUsage(data, symCode)
    entropy, length = compareLengthEntropy(data, symCode, pmf)

    print("\n")
    
    print("Encoding and Decoding calculating frequencies")
    outputEnc, huffmanTree, symCode = huffmanEncode(data)
    huffmanDecode(outputEnc, huffmanTree)
    #print("Decoded output:", huffmanDecode(outputEnc, huffmanTree))
    compareSpaceUsage(data, symCode)
    entropy, length = compareLengthEntropy(data, symCode)
    print("\n")'''

    
       
    '''# read from a file to calculate frequencies (estimated pmf)
    with open("data.txt", "w") as f:
        for item in data:
            f.write("%s" % item)
    f = open("data.txt", "rb")
    data_read = []
    while bytes := f.read(1):
        data_read.append(bytes)
        
    print("Encoding and decoding after having calculated the frequences from a file")
    outputEnc, huffmanTree, symCode = huffmanEncode(data_read)    
    print("Decoded output:", huffmanDecode(outputEnc, huffmanTree))
    compareSpaceUsage(data_read, symCode)
    entropy, length = compareLengthEntropy(data_read, symCode)'''
    
    
    
    
    
    
    
    
    
    #parte momentaneamente spostata in appoggio.py
    
    
    
    
    
    
    
   
        
        
        
        
        
    '''lorem = [1, 2, 5, 10, 30, 100, 300, 500, 700, 999]
    for i in range(len(lorem)):
        print("\n Huffman algorithm with lorem"+str(lorem[(i)])+".txt")
        file = open("../files/lorem/lorem"+str(lorem[(i)])+".txt", "rb")
        data = []
        while bytes := file.read(1):
            data.append(bytes)
        #print("pmf bytes", pmf)
        t1 = time.time()
        outputEnc, huffmanTree, symCode = huffmanEncode(data)
        t2 = time.time()
        print("Encoding time:", t2 - t1)
        #print(symCode)
        #print("Encoded output:", outputEnc)
        t1 = time.time()
        huffmanDecode(outputEnc, huffmanTree)
        t2 = time.time()
        print("Decoding time:", t2 - t1)
        #print("Decoded Output:", huffmanDecode(outputEnc, huffmanTree))
        compareSpaceUsage(data, symCode)
        #print("symCode:", symCode)
        entropy, length = compareLengthEntropy(data, symCode)
        #n.append(x)'''
        
        #entropies.append(entropy)
        #entropies1.append(entropy + 1 / x)
        
    #plotLengthEntropy(n, entropies, lengths, entropies1, entropiesT)
    
    '''numChar = [932, 1377, 4210, 7546, 21917, 75889, 227833, 383458, 521852, 751679]
    huffCompr = [47.21, 47.25, 47.02, 47.008, 47.036, 47.005, 46.97, 46.95, 46.98, 46.96]
    LZCompr = [-11.17, -7.42, 0.93, 6.58, 14.17, 23.78, 31.98, 36.72, 39.53, 42.81]
    huffEncTime = [0.001, 0.001, 0.001, 0.0035, 0.01, 0.0346, 0.09, 0.19, 0.37, 0.63]
    LZEncTime = [0.003, 0.006, 0.018, 0.03, 0.07, 0.22, 0.72, 1.35, 1.97, 3.12]
    huffDecTime = [0.001, 0.001, 0.0025, 0.006, 0.02, 0.0711, 0.177, 0.35, 0.57, 0.93]
    LZDecTime = [0.001, 0.003, 0.005, 0.01, 0.04, 0.1, 0.34, 0.69, 1.08, 2.05]
    
    plotCompression(numChar, huffCompr, LZCompr)
    plotEncTime(numChar, huffEncTime, LZEncTime)
    plotDecTime(numChar, huffDecTime, LZDecTime)
'''
    