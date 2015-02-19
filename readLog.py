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

    for fmt, _, l in bitStruct:
        assert(int(fmt.split(':')[1]) == l)


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


def getLogEntryFromDevice(le_index=120):
    
    assert(0 < le_index <= 120)  # First index is 1 (not 0)
    
    # amp = LakePP("169.254.166.60", "d3000015:6b44ed00")
    amp = LakePP("127.0.0.1", "BEE7ACE5:55E78008")

    le_NumberOfEnts  = 120
    le_Length        = 112
    le_BaseAddr      = 0x70002
    le_ToRead        = le_BaseAddr + le_Length * (le_index-1)  # Oldest entry is in the beginning, we want the newest/last
    le_AddrRange     = range(le_ToRead, (le_ToRead + le_Length))
    assert(le_AddrRange[-1] == 0x073481)

    return [amp.read_param(a)[0] for a in le_AddrRange]


def test_ValidLogDict(logDict):
    assert(logDict['ucTag0'] == ord('L'))
    assert(logDict['ucTag1'] == ord('O'))
    assert(logDict['ucTag2'] == ord('G'))

if __name__ == '__main__':

    test_bitStruct(bitStruct)

    fefefe = splitBitStructIn32bits(bitStructIter)
    logDict = OrderedDict()
    logEntry = map(str, getLogEntryFromDevice())
    assert(len(logEntry) == 112)

    for logE in logEntry:
        rawBits = BitArray('int:32=' + logE)
        ent = next(fefefe)
        b = rawBits.unpack(entryToFmtString(ent))
        for (k, v) in zip(ent, b):
            logDict[k[1]] = v

    test_ValidLogDict(logDict)
    # print logDict
    print 'ucChksum: ', logDict['ucChksum']
    print 'uiTimestamp: ', logDict['uiTimestamp']
    print 'global.accWatisar: ', logDict['global.accWatisar']
    print 'ChLogEntry_ChA.usPtgZ0: ', logDict['ChLogEntry_ChA.usPtgZ0']
    print 'ChLogEntry_ChA.usPtgZ1: ', logDict['ChLogEntry_ChA.usPtgZ1']
    print 'ChLogEntry_ChB.usPtgZ0: ', logDict['ChLogEntry_ChB.usPtgZ0']
    print 'ChLogEntry_ChB.usPtgZ1: ', logDict['ChLogEntry_ChB.usPtgZ1']
    print 'ChLogEntry_ChC.usPtgZ0: ', logDict['ChLogEntry_ChC.usPtgZ0']
    print 'ChLogEntry_ChC.usPtgZ1: ', logDict['ChLogEntry_ChC.usPtgZ1']
    print 'ChLogEntry_ChD.usPtgZ0: ', logDict['ChLogEntry_ChD.usPtgZ0']
    print 'ChLogEntry_ChD.usPtgZ1: ', logDict['ChLogEntry_ChD.usPtgZ1']

