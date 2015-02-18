# from lakeffi_util import LakeAPI
# from time import sleep
from bitstring import BitArray
from bitStruct import bitStructIter, bitStruct
from collections import OrderedDict
from lakeapi.lakepp import LakePP


def test_bitStruct(bitStruct):
    summa = sum([x[2] for x in bitStruct])
    assert(summa % 32 == 0)
    assert(summa / 32 == 112)


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
    # amp = LakePP("169.254.166.60", "d3000015:6b44ed00")
    amp = LakePP("127.0.0.1", "BEE7ACE5:55E78008")

    logEnteryBaseAddr = 0x70002
    logEnteryAddrRange = range(logEnteryBaseAddr, (logEnteryBaseAddr + 112))

    return [amp.read_param(a)[0] for a in logEnteryAddrRange]


if __name__ == '__main__':

    test_bitStruct(bitStruct)

    fefefe = splitBitStructIn32bits(bitStructIter)
    logDict = OrderedDict()
    logEntry = map(str, getLogEntryFromDevice())
    assert(len(logEntry) == 112)
    print logEntry

    for logE in logEntry:
        rawBits = BitArray('int:32=' + logE)
        ent = next(fefefe)
        b = rawBits.unpack(entryToFmtString(ent))
        for (k, v) in zip(ent, b):
            logDict[k[1]] = v

    print logDict
    print logDict['global.accWatisar']
    print logDict['ChLogEntry_ChB.usPtgZ0']
    print logDict['ChLogEntry_ChB.usPtgZ1']
