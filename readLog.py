# from lakeffi_util import LakeAPI
# from time import sleep
# from bitstring import ConstBitStream, BitArray
from bitStruct import bitStructIter 




def splitBitStructToWords(bitStruct):
    acc = 0
    accList = []
    for bS in bitStruct:
        accList.append(bS)
        acc += bS[2]
        if(acc >= 32):
            acc = 0
            yield accList
            accList = []



if __name__ == '__main__':
    # p = LakeAPI("127.0.0.1", "BEE7ACE5:55E78008")
    # p = LakeAPI("169.254.166.60", "D3000015:6B44ED00")

    # try:
    #   print p.p20_peek(0x100000,2)
    # except LakeAPI.error as e:
    #   print p.returnCodeToText(int(e.message))

    # try:
    #   print p.dlm_param("Dev.FrameLabel?")
    # except LakeAPI.error as e:
    #   print p.returnCodeToText(int(e.message))

    # logEntry = p.p20_peek(0x73412,112)
    print type(bitStructIter)
    fefefe = splitBitStructToWords(bitStructIter)
    print type(fefefe)

    i = 0
    for fe in fefefe:
        print i
        print fe
        i += 1

    logEntry = map(hex, [1280263945, 6, 0, 1, 59456, 389930, 42618, 578,
                         3903, 0, 504870, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, -1229605884, 73293312, 394248, 269484032, 0,
                         0, 33554432, 387317760, 0, 5910, 0, 0, 0, 268,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 387383296,
                         0, 5911, 0, 0, 0, 187, 0, 0])
    print len(logEntry)

    fmt = 'bytes:3, int:8, uint'
    d = ['text', 'checksum', 'test']

    print logEntry
    tString = logEntry[0] + ', ' + logEntry[1] + ', ' + logEntry[2]
    tString = '0x4c4f4709, 0x02'
    tString = 'int:32=1280263945, int:32=6'
    print tString
    s = BitArray(tString)
    print s
    b = s.unpack(fmt)

    print {k: v for (k, v) in zip(d, b)}
