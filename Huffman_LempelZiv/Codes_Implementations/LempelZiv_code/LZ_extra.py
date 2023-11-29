from math import log
from fractions import Fraction
import matplotlib.pyplot as plt


def compareSpaceUsage(data, outputEnc):
    """Utility function that calculates the comparison between space occupied by compressed and uncompressed data

    Args:
        data: data containing all symbols
        symCode: symbols and Huffman codes dictionary
    """
    # total bit space to store data
    beforeCompressionBit = len(data)    
    beforeCompressionByte = beforeCompressionBit // 8
    afterCompressionBit = len(outputEnc)
    afterCompressionByte = afterCompressionBit // 8
    print("Space usage before compression:", beforeCompressionBit,
          "bits (" + str(beforeCompressionByte) + " Bytes)")
    print("Space usage after compression:", afterCompressionBit,
          "bits (" + str(afterCompressionByte) + " Bytes)")
    print("Compression gain:", beforeCompressionBit - afterCompressionBit,
          "bits (" + str(beforeCompressionByte - afterCompressionByte) + " Bytes)")
    print("Compression ratio:", round(
        (1 - afterCompressionBit / beforeCompressionBit) * 100, 8), "%")
    return round((1 - afterCompressionBit / beforeCompressionBit) * 100, 8)


'''def calculateEntropy(symFreq, tot):
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

    return round(entropy, 8)'''


def calculateCodesMeanLength(symFreq, tot, symCode):
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
        codesMeanLength += len(symCode[symbol]) * \
            Fraction(symFreq[symbol], tot)

    return round(float(codesMeanLength), 8)


'''def compareLengthEntropy(data, symCode):
    """Utility function that calculates the comparison between entropy and codes statistic mean length

    Args:
        data: data containing all symbols
        symCode: symbols and Huffman codes dictionary
    
    Returns:
        entropy: entropy value of data
        codesMeanLength: codes statistic mean length
    """
    symFreq = calculateFrequencies(data)
    tot = len(data)

    entropy = calculateEntropy(symFreq, tot)
    codesMeanLength = calculateCodesMeanLength(symFreq, tot, symCode)

    print("Entropy:", entropy)
    print("Codes mean length:", codesMeanLength)
    print("Difference:", round(codesMeanLength - entropy, 8))

    return entropy, codesMeanLength'''


def plotLengthEntropy(n, entropies, lengths):
    plt.plot(n, entropies)
    plt.plot(n, lengths)
    plt.show()