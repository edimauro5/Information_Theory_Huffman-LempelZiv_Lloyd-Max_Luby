#per final.py
from Codes_Implementations.Huffman_code.Huffman import *
from Codes_Implementations.Huffman_code.Huffman_extra import *

#from Huffman import *
#from Huffman_extra import *
from math import log
from fractions import Fraction
import matplotlib.pyplot as plt
from scipy.stats import entropy


def compareSpaceUsage(data, symCode):
    """Utility function that calculates the comparison between space occupied by compressed and uncompressed data

    Args:
        data: data containing all symbols
        symCode: symbols and Huffman codes dictionary
    """
    # total bit space to store data
    beforeCompressionByte = len(data)
    beforeCompressionBit = beforeCompressionByte * 8
    afterCompressionBit = 0
    symbols = symCode.keys()
    for symbol in symbols:
        count = data.count(symbol)
        # calculate how many bits are required for that symbol in total
        afterCompressionBit += count * len(symCode[symbol])
    afterCompressionByte = afterCompressionBit / 8
    print("Space usage before compression:", beforeCompressionBit,
          "bits (" + str(beforeCompressionByte) + " Bytes)")
    print("Space usage after compression:", afterCompressionBit,
          "bits (" + str(afterCompressionByte) + " Bytes)")
    print("Compression gain:", beforeCompressionBit - afterCompressionBit,
          "bits (" + str(beforeCompressionByte - afterCompressionByte) + " Bytes)")
    print("Compression ratio:", round(
        (1 - afterCompressionBit / beforeCompressionBit) * 100, 8), "%")
    return round((1 - afterCompressionBit / beforeCompressionBit) * 100, 8)

def calculateEntropy(symFreq, tot):
    """Utility function that calculates the entropy value of data

    Args:
        symFreq: symbols and frequencies dictionary
        tot: data length

    Returns:
        entropy: entropy value of data
    """
    entropy = 0

    for frequency in list(symFreq.values()):
        pk = Fraction(frequency, tot)
        entropy -= pk * log(pk, 2)

    return round(entropy, 8)


def calculateCodesMeanLength(symFreq, tot, symCode, pmf=None):
    """Utility function that calculates the codes statistic mean length

    Args:
        symFreq: symbols and frequencies dictionary
        tot: data length
        symCode: symbols and Huffman codes dictionary

    Returns:
        codesMeanLength: codes statistic mean length
    """
    codesMeanLength = 0
    
    for symbol in list(symCode.keys()):
        if pmf != None:
            codesMeanLength += len(symCode[symbol]) * symFreq[symbol]
        else:
            codesMeanLength += len(symCode[symbol]) * \
        Fraction(symFreq[symbol], tot)               

    return round(float(codesMeanLength), 8)


def compareLengthEntropy(symCode, pmf=None, data=None):
    """Utility function that calculates the comparison between entropy and codes statistic mean length

    Args:
        data: data containing all symbols
        symCode: symbols and Huffman codes dictionary
    
    Returns:
        entropy: entropy value of data
        codesMeanLength: codes statistic mean length
    """
    if pmf != None:
        symFreq = pmf
        tot = len(list(pmf.keys()))
    else:
        symFreq = calculateFrequencies(data)
        tot = len(data)
    

    if pmf != None:
        entr = entropy(list(pmf.values()), base=2)
    else:
        #entr = calculateEntropy(symFreq, tot)
        entr = entropy(list(symFreq.values()), base=2)
    #entr = entropy(list(pmf1.values()))
    codesMeanLength = calculateCodesMeanLength(symFreq, tot, symCode, pmf)

    print("Entropy:", entr)
    print("Codes mean length:", codesMeanLength)
    print("Difference:", round(codesMeanLength - entr, 8))

    return entr, codesMeanLength


def plotLengthEntropy(n, entropiesT, lengths, entropies1):
    plt.plot(n, entropiesT, label="H(X)")
    plt.plot(n, lengths, label="L")
    plt.plot(n, entropies1, label="H(X)+1/n")
    plt.xlabel("n")
    plt.legend()
    plt.show()
    
def plotLengthEntropyEst(n, entropies, lengths, entropies1):
    plt.plot(n, entropies, label="Estimated H(X)")
    plt.plot(n, lengths, label="L")
    plt.plot(n, entropies1, label="Estimated H(X)+1/n")
    plt.xlabel("n")
    plt.legend()
    plt.show()
    
def plotCompression(source_size, huffCompr, LZCompr):
    plt.figure(1)
    plt.plot(source_size, huffCompr, label = "Huffman")
    plt.plot(source_size, LZCompr, label = "LZ")
    
    plt.xlabel("Input size [KB]")
    plt.ylabel("Compression ratio [%]")
    plt.legend()
    plt.show()
    
def plotCompressionHuff(numChar, huffCompr):
    plt.figure(7)
    plt.plot(numChar, huffCompr, label = "Huffman")
    
    plt.xlabel("n")
    plt.ylabel("Compression ratio [%]")
    plt.legend()
    plt.show()
    
def plotEncTime(numChar, huffEncTime, LZEncTime):
    plt.figure(2)
    plt.plot(numChar, huffEncTime, label = "Huffman")
    plt.plot(numChar, LZEncTime, label = "LZ")    
    plt.xlabel("n")
    plt.ylabel("Encoding time [s]")
    plt.legend()
    
    plt.show(block=False)
    
def plotDecTime(numChar, huffDecTime, LZDecTime):
    plt.figure(3)
    plt.plot(numChar, huffDecTime, label = "Huffman")
    plt.plot(numChar, LZDecTime, label = "LZ")
    
    plt.xlabel("n")
    plt.ylabel("Decoding time [s]")
    plt.legend()
    plt.show()
    
def pltEntrCompr(sizes, entropies, compressions):
    plt.figure(4)
    plt.plot(sizes, entropies, label = "Entropy")
    plt.plot(sizes, compressions, label = "Compression ratio")
    
    plt.xlabel("size")
    plt.legend()
    plt.show()
    
def pltEntrJoint(n, jointEntropiesT, joinEntropiesEst):
    plt.figure(5)
    plt.plot(n, jointEntropiesT, label = "H(X1, ..., Xn)")
    plt.plot(n, joinEntropiesEst, label = "Estimated H(X1, ..., Xn)")
    
    plt.xlabel("n")
    plt.legend()
    plt.show()
    
def pltEntrTEntrEst(n, entropiesT, entropies):
    plt.figure(6)
    plt.plot(n, entropiesT, label = "H(X)")
    plt.plot(n, entropies, label = "Estimated H(X)")
    
    plt.xlabel("n")
    plt.legend()
    plt.show()