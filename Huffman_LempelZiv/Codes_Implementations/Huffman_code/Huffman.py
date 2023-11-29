import heapq


class Node:
    def __init__(self, frequency, symbol, left=None, right=None):
        """Node constructor

        Args:
            frequency: frequency of symbol
            symbol: symbol name
            left: left node of current node. Defaults to None
            right: right node of current node. Defaults to None
        """
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        # tree direction (0/1)
        self.code = ''

    def __lt__(self, next):
        """Method used to define or implement the functionality of the less than operator “<”. It compares two frequency attributes

        Args:
            next: operand compared to the current one

        Returns:
            True or False depending on the comparison
        """
        return self.frequency < next.frequency


def calculateFrequencies(data):
    """Utility function that calculates the frequency for all symbols in data

    Args:
        data: data containing all symbols

    Returns:
        symFreq: symbols and frequencies dictionary
    """
    symFreq = dict()
    for element in data:
        if symFreq.get(element) is None:
            symFreq[element] = 1
        else:
            symFreq[element] += 1
    return symFreq


def createHuffmanTree(nodes, pmf=None, data=None):
    """Utility function that creates the Huffman tree using data

    Args:
        data: data containing all symbols
        nodes: list containing all Huffman tree nodes
    """
    if pmf != None:
        symFreq = pmf
    else:
        symFreq = calculateFrequencies(data)
    symbols = list(symFreq.keys())
    frequencies = list(symFreq.values())

    # convert symbols and frequencies into Huffman tree nodes
    for x in range(len(symbols)):
        heapq.heappush(nodes, Node(frequencies[x], symbols[x]))

    while len(nodes) > 1:
        # remove the two nodes with the smallest frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # assign directional value to these nodes
        left.code = 0
        right.code = 1

        # combine these nodes to create a new one
        newNode = Node(left.frequency + right.frequency,
                       left.symbol + right.symbol, left, right)

        heapq.heappush(nodes, newNode)


def calculateCodes(huffmanTree, symCode, partialCode=''):
    """Utility function that calculates the Huffman codes for all symbols by traveling the Huffman tree

    Args:
        huffmanTree: Huffman tree root
        symCode: symbols and Huffman codes dictionary
        partialCode: Huffman code string of a symbol to update. Defaults to ''
    """
    partialCode += str(huffmanTree.code)

    if huffmanTree.left:
        calculateCodes(huffmanTree.left, symCode, partialCode)
    if huffmanTree.right:
        calculateCodes(huffmanTree.right, symCode, partialCode)
    if not huffmanTree.left and not huffmanTree.right:
        symCode[huffmanTree.symbol] = partialCode


def encodeData(data, symCode):
    """Utility function that prints the output using the Huffman codes for all symbols of data

    Args:
        data: data containing all symbols
        symCode: symbols and Huffman codes dictionary

    Returns:
        outputEnc: output encoded string
    """
    outputEnc = ""
    for element in data:
        outputEnc += str(symCode[element])

    return outputEnc


def huffmanEncode(pmf=None, data=None):
    """Method that encodes data

    Args:
        data: data containing all symbols

    Returns:
        outputEnc: output encoded string
        nodes[0]: Huffman tree root
        symCode: symbols and Huffman codes dictionary
    """
    nodes = []
    symCode = dict()

    createHuffmanTree(nodes, pmf, data)
    calculateCodes(nodes[0], symCode)
    outputEnc = encodeData(data, symCode)
    return outputEnc, nodes[0], symCode


def huffmanDecode(outputEnc, huffmanTree):
    """Method that decodes data

    Args:
        outputEnc: output encoded string
        huffmanTree: Huffman tree root

    Returns:
        outputDec: output decoded string
    """
    root = huffmanTree
    outputDec = ""
    for bit in outputEnc:
        if bit == '1':
            huffmanTree = huffmanTree.right
        elif bit == '0':
            huffmanTree = huffmanTree.left
        if huffmanTree.left is None and huffmanTree.right is None:
            outputDec += str(huffmanTree.symbol)
            huffmanTree = root

    return outputDec
