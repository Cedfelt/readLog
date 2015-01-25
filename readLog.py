# from lakeffi_util import LakeAPI
# from time import sleep
from bitstring import BitArray
from bitStruct import bitStructIter


def splitBitStructIn32bits(bitStruct):
    acc = 0
    accList = []
    for bS in bitStruct:
        accList.append(bS)
        acc += bS[2]
        if(acc >= 32):
            assert(acc == 32)
            acc = 0
            yield accList
            accList = []


def entryToFmtString(entry):
    rString = ""
    for e in entry:
        rString += e[0] + ", "
    return rString


def getLogEntryFromDevice():
    p = LakeAPI("127.0.0.1", "BEE7ACE5:55E78008")
    p = LakeAPI("169.254.166.60", "D3000015:6B44ED00")

    return p.p20_peek(0x73412, 112)


if __name__ == '__main__':

    fefefe = splitBitStructIn32bits(bitStructIter)

    # logEntry = getLogEntryFromDevice()
    logEntry = map(str, [1280263945, 6, 0, 1, 59456, 389930, 42618, 578,
                         3903, 0, 504870, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, -1229605884, 73293312, 394248, 269484032, 0,
                         0, 33554432, 387317760, 0, 5910, 0, 0, 0, 268,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 387383296,
                         0, 5911, 0, 0, 0, 187, 0, 0])

    for logE in logEntry:
        rawBits = BitArray('int:32=' + logE)
        ent = next(fefefe)
        b = rawBits.unpack(entryToFmtString(ent))
        print {k[1]: v for (k, v) in zip(ent, b)}
        print
