# from lakeffi_util import LakeAPI
# from time import sleep
from bitstring import BitArray
from bitStruct import bitStructIter, bitStruct
from collections import OrderedDict
from lakeapi.lakepp import LakePP
import time


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
    # amp = LakePP("127.0.0.1", "BEE7ACE5:55E78008")
    amp = LakePP("169.254.97.224")

    le_NumberOfEnts  = 120
    le_Length        = 112
    le_BaseAddr      = 0x70002
    le_ToRead        = le_BaseAddr + le_Length * (le_index-1)  # Oldest entry is in the beginning, we want the newest/last
    le_AddrRange     = range(le_ToRead, (le_ToRead + le_Length))
    assert(le_AddrRange[-1] == 0x073481)

    #return amp.read_params(hex(le_ToRead), le_Length)
    return [amp.read_param(hex(a)) for a in le_AddrRange]


def test_ValidLogDict(logDict):
    assert(logDict['ucTag0'] == ord('L'))
    assert(logDict['ucTag1'] == ord('O'))
    assert(logDict['ucTag2'] == ord('G'))

if __name__ == '__main__':

    test_bitStruct(bitStruct)

    for _ in range(1):
        fefefe = splitBitStructIn32bits(bitStruct)
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
        print 'ucChksum: ', hex(logDict['ucChksum'])
        print 'ucVer: ', logDict['ucVer']
        print 'uiTimestamp: ', logDict['uiTimestamp']
        print 'global.accWatisar: ', logDict['global.accWatisar']
        print 'ChLogEntry_ChA.ucThermHR: ', logDict['ChLogEntry_ChA.ucThermHR']
        print 'ChLogEntry_ChA.usMinLoadZ0: ', logDict['ChLogEntry_ChA.usMinLoadZ0']
        print 'ChLogEntry_ChA.usMaxLoadZ0: ', logDict['ChLogEntry_ChA.usMaxLoadZ0']
        print 'ChLogEntry_ChA.usMinLoadZ1: ', logDict['ChLogEntry_ChA.usMinLoadZ1']
        print 'ChLogEntry_ChA.usMaxLoadZ1: ', logDict['ChLogEntry_ChA.usMaxLoadZ1']
        print ''
        print 'ChLogEntry_ChB.usMinLoadZ0: ', logDict['ChLogEntry_ChB.usMinLoadZ0']
        print 'ChLogEntry_ChB.usMaxLoadZ0: ', logDict['ChLogEntry_ChB.usMaxLoadZ0']
        print 'ChLogEntry_ChB.usMinLoadZ1: ', logDict['ChLogEntry_ChB.usMinLoadZ1']
        print 'ChLogEntry_ChB.usMaxLoadZ1: ', logDict['ChLogEntry_ChB.usMaxLoadZ1']
        print ''
        print 'ChLogEntry_ChC.usMinLoadZ0: ', logDict['ChLogEntry_ChC.usMinLoadZ0']
        print 'ChLogEntry_ChC.usMaxLoadZ0: ', logDict['ChLogEntry_ChC.usMaxLoadZ0']
        print 'ChLogEntry_ChC.usMinLoadZ1: ', logDict['ChLogEntry_ChC.usMinLoadZ1']
        print 'ChLogEntry_ChC.usMaxLoadZ1: ', logDict['ChLogEntry_ChC.usMaxLoadZ1']
        print ''
        print 'ChLogEntry_ChD.usMinLoadZ0: ', logDict['ChLogEntry_ChD.usMinLoadZ0']
        print 'ChLogEntry_ChD.usMaxLoadZ0: ', logDict['ChLogEntry_ChD.usMaxLoadZ0']
        print 'ChLogEntry_ChD.usMinLoadZ1: ', logDict['ChLogEntry_ChD.usMinLoadZ1']
        print 'ChLogEntry_ChD.usMaxLoadZ1: ', logDict['ChLogEntry_ChD.usMaxLoadZ1']
        # print 'ChLogEntry_ChC.usMinLoadZ0: ', logDict['ChLogEntry_ChC.usMinLoadZ0']
        # print 'ChLogEntry_ChC.usMaxLoadZ0: ', logDict['ChLogEntry_ChC.usMaxLoadZ0']
        # print 'ChLogEntry_ChD.usMinLoadZ0: ', logDict['ChLogEntry_ChD.usMinLoadZ0']
        # print 'ChLogEntry_ChD.usMaxLoadZ0: ', logDict['ChLogEntry_ChD.usMaxLoadZ0']
        # print 'ChLogEntry_ChC.usMinLoadZ1: ', logDict['ChLogEntry_ChC.usMinLoadZ1']
        # print 'ChLogEntry_ChC.usMaxLoadZ1: ', logDict['ChLogEntry_ChC.usMaxLoadZ1']
        # print 'ChLogEntry_ChD.usMinLoadZ1: ', logDict['ChLogEntry_ChD.usMinLoadZ1']
        # print 'ChLogEntry_ChD.usMaxLoadZ1: ', logDict['ChLogEntry_ChD.usMaxLoadZ1']
        
        time.sleep(2)

