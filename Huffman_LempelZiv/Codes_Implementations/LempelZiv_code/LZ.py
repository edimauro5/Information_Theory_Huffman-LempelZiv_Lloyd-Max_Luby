def lzEncode(data):
    phrAddr = {}
    phrase = ''
    addr = 1
    k = -1
    i = 0
    outputEnc = ''
    for bit in data:
        phrase += str(bit)
        if phrase not in phrAddr.keys():
            phrAddr[phrase] = addr
            addr += 1
            if k == -1:
                prefAddr = ''
                k += 1
            elif i <= pow(2, k):
                if i == pow(2, k):
                    k += 1
                    i = 0
                if len(phrase) == 1:
                    prefAddr = str(bin(0)[2:].zfill(k + 1))
                else:
                    prefAddr = str(bin(phrAddr[phrase[:-1]])[2:].zfill(k + 1))
                i += 1
            outputEnc += prefAddr + phrase[-1]
            phrase = ''
    if len(phrase) > 0:
        print(phrase)
        outputEnc += phrase
    return outputEnc, len(phrase)


def lzDecode(outputEnc, lenEnd):
    k = -1
    i = 0
    count = 0
    addr = 1
    addrPhr = {}
    code = ''
    outputDec = ''
    end = outputEnc[-lenEnd:]
    for bit in outputEnc:
        code += bit
        if k == -1:
            outputDec += code
            addrPhr[addr] = code
            k += 1
            code = ''
            addr += 1
        elif i == k + 1:
            addrPref = int(code[:-1], 2)
            if addrPref in addrPhr.keys():
                pref = addrPhr[addrPref]
            else:
                pref = ''
            phrase = pref + code[-1]
            outputDec += phrase
            addrPhr[addr] = phrase
            code = ''
            addr += 1
            count += 1
            i = 0
            if count == pow(2, k):
                k += 1
                count = 0
        else:
            i += 1
    outputDec += end
    return outputDec
